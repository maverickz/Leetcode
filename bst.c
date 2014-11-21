#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>
#include <sys/queue.h>

#define MAX(a,b) (((a)>(b))?(a):(b))

TAILQ_HEAD(tailhead, tree_node_s) head =
     TAILQ_HEAD_INITIALIZER(head);
struct tailhead *headp;

typedef struct tree_node_s {
    int value;
    struct tree_node_s *parent;
    struct tree_node_s *left;
    struct tree_node_s *right;
    TAILQ_ENTRY(tree_node_s) entries;
} tree_node_t;

int post_index = 0;

void inorder(tree_node_t *root) {
    if (!root) {
        return;
    }
    inorder(root->left);
    printf("%d [%d, %d]\n", root->value, root->left?root->left->value:0, root->right?root->right->value:0);
    inorder(root->right);
}

void serialize(tree_node_t *root, char *buffer)
{
    if (root == NULL) {
        strcat(buffer, "# ");
        return;
    }
    char number[64];
    sprintf(number, "%d ", root->value);
    strcat(buffer, number);
    serialize(root->left, buffer);
    serialize(root->right, buffer);
}

char **tokenize(char *buffer, int *num_tokens)
{
    int i;
    char **tokens = NULL;
    char *token = NULL;
    char *tmp = strdup(buffer);
    tokens = (char **)calloc(1, strlen(buffer));

    for (i = 0; i < strlen(buffer); i++) {
        tokens[i] = (char *)calloc(1,64);
    }
    token = strtok(tmp, " ");
    while (token) {
        snprintf(tokens[(*num_tokens)++], 64, "%s", token);
        token = strtok(NULL, " ");
    }
    tokens = (char **)realloc(tokens, *num_tokens);
    return tokens;
}

tree_node_t *deserialize(char **tokens, int num_tokens)
{
    static int token_index = 0;
    if (token_index >= num_tokens) {
        return NULL;
    }
    if (strcmp(tokens[token_index], "#") == 0) {
        token_index++;
        return NULL;
    } else {
        tree_node_t *node = calloc(1, sizeof(tree_node_t));
        node->value = atoi(tokens[token_index++]);
        node->left = deserialize(tokens, num_tokens);
        node->right = deserialize(tokens, num_tokens);
        return node;
    }
}

int serialize_inorder(tree_node_t *root, int array[]) 
{
    static int index = 0;
    if (root == NULL) {
        return 0;
    }
    serialize_inorder(root->left, array);
    array[index++] = root->value;
    serialize_inorder(root->right, array);
    return index;
}

int serialize_preorder(tree_node_t *root, int array[]) 
{
    static int index = 0;
    if (root == NULL) {
        return 0;
    }
    array[index++] = root->value;
    serialize_preorder(root->left, array);
    serialize_preorder(root->right, array);
    return index;
}

int serialize_postorder(tree_node_t *root, int array[]) {
    static int index = 0;
    if (root == NULL) {
        return 0;
    }
    serialize_postorder(root->left, array);
    serialize_postorder(root->right, array);
    array[index++] = root->value;
    return index;
}

int find_index(int array[], int target, int start, int end)
{
    int i;
    for (i = 0; i <= end; i++) {
        if (array[i] == target) {
            return i;
        }
    }
    return -1;
}

tree_node_t *deserialize_preorder(int inorder_array[], int preorder_array[], int start, int end)
{
    static int pre_index = 0;
    if (start > end) {
        return NULL;
    }

    tree_node_t *node = calloc(1, sizeof(tree_node_t));
    int target = preorder_array[pre_index++];
    node->value = target;
    if (start == end) {
        return node;
    }
    int inorder_index = find_index(inorder_array, target, start, end);
    node->left = deserialize_preorder(inorder_array, preorder_array, start, inorder_index - 1);
    node->right = deserialize_preorder(inorder_array, preorder_array, inorder_index + 1, end);
    return node;
}

tree_node_t *deserialize_postorder(int inorder_array[], int postorder_array[], int start, int end)
{
    if (start > end || post_index < 0) {
        return NULL;
    }

    tree_node_t *node = calloc(1, sizeof(tree_node_t));
    int target = postorder_array[post_index--];
    node->value = target;

    if (start == end) {
        return node;
    }
    int inorder_index = find_index(inorder_array, target, start, end);
    node->right = deserialize_postorder(inorder_array, postorder_array, inorder_index + 1, end);
    node->left = deserialize_postorder(inorder_array, postorder_array, start, inorder_index - 1);
    return node;
}

tree_node_t *insert(tree_node_t *root, tree_node_t *parent, int value)
{
    if (root == NULL) {
        tree_node_t *new_node = calloc(1, sizeof(tree_node_t));
        new_node->value = value;
        root = new_node;
        root->parent = parent;
    } else if (root->value > value) {
        root->left = insert(root->left, root, value);
    } else {
        root->right = insert(root->right, root, value);
    }
    return root;
}

tree_node_t *search(tree_node_t *root, int value)
{
    if (!root) {
        return NULL;
    } else if (root->value > value) {
        return search(root->left, value);
    } else if (root->value < value) {
        return search(root->right, value);
    } else {
        return root;
    }
}

tree_node_t *find_min_node(tree_node_t *root)
{
    tree_node_t *curr_node = root;
    while (curr_node->left) {
        curr_node = curr_node->left;
    }
    return curr_node;
}

tree_node_t *delete(tree_node_t *root, int value) 
{
    if (root == NULL) {
        return root;
    } else if (root->value > value) {
        root->left = delete(root->left, value);
    } else if (root->value < value) {
        root->right = delete(root->right, value);
    } else {
        if (root->left && root->right) {
            tree_node_t *successor = find_min_node(root->right);
            root->value = successor->value;
            root->right = delete(root->right, root->value);
        } else {
            tree_node_t *tmp = root;
            if (root->left == NULL) {
                root = root->right;
            } else if (root->right == NULL) {
                root = root->left;
            } 
            free(tmp);
        }
    }
    return root;  
}

bool isBST(tree_node_t *root, int min, int max)
{
    if (root == NULL) {
        return true;
    }
    if (!(root->value >= min && root->value <= max)) {
        return false;
    } else {
        return isBST(root->left, min, root->value) && isBST(root->right, root->value, max);
    }
}

bool compare(tree_node_t *T1, tree_node_t *T2)
{
    if (T1 == NULL && T2 == NULL) {
        return true;
    } else {
        if ((T1 && T2 == NULL) || (T2 && T1 == NULL)) {
            return false;
        }
        if (T1->value != T2->value) {
            return false;
        } else {
            return compare(T1->left, T2->left) && compare(T1->right,T2->right);
        }
    }
}

int count_nodes(tree_node_t *root)
{
    if (root == NULL) {
        return 0;
    } 
    return (1 + count_nodes(root->left) + count_nodes(root->right));
}

int height(tree_node_t *root)
{
    if (root == NULL) {
        return -1;
    } else {
        printf("LEFT: %d\n", height(root->left));
        return (1 + MAX(height(root->left), height(root->right)));
    }
}

int kth_samllest_element(tree_node_t *root, int k)
{
    if (root == NULL) {
        return 0;
    }
    int left_tree_size = 0;
    left_tree_size = count_nodes(root->left);

    if (k == left_tree_size + 1) {
        return root->value;
    } else if (k <= left_tree_size) {
        return kth_samllest_element(root->left, k);
    } else {
        return kth_samllest_element(root->right, k - left_tree_size - 1);
    }
}

void display(tree_node_t *root, int array[], int n)
{
    int i;
    printf("*******************************************************\n");
    for (i = 0; i < n; i++) {
        tree_node_t *node = search(root, array[i]);
        printf ("Key: %d, Value:%d, Address:%p\n", array[i], node?node->value:-1, node);
    }
    printf("*******************************************************\n");
}

void display_array(int array[], int len)
{
    int i;
    for (i = 0; i < len; i++) {
        printf("%d\t", array[i]);
    }
    printf("\n");
}

void bfs(tree_node_t *root)
{
    if (root == NULL) {
        return;
    }
     tree_node_t *curr_node = root;
     TAILQ_INIT(&head);
     TAILQ_INSERT_HEAD(&head, curr_node, entries);
     int curr_level = 1;
     int next_level = 0;
     while (!TAILQ_EMPTY(&head)) {
         curr_node = TAILQ_FIRST(&head);
         TAILQ_REMOVE(&head, curr_node, entries);
         printf("%d ", curr_node->value);
         curr_level--;

         if (curr_node->left) {
            TAILQ_INSERT_TAIL(&head, curr_node->left, entries);
            next_level++;
         }

         if (curr_node->right) {
            TAILQ_INSERT_TAIL(&head, curr_node->right, entries);
            next_level++;
         }

         if (curr_level == 0) {
            curr_level = next_level;
            next_level = 0;
            printf("\n");
         }
     }
}

void dfs(tree_node_t *root)
{
    if (root) {
        if (root->left){
            dfs(root->left); 
        }
        if (root->right) {
            dfs(root->right);
        }
        printf("%d ", root->value);
    } else {
        return;
    }

tree_node_t *LCA(tree_node_t *root, int p, int q)
{
    if (root == NULL) {
        return NULL;
    }

    if (root->value == p || root->value == q) {
        return root;
    }

    tree_node_t *LCA_left = LCA(root->left, p, q);
    tree_node_t *LCA_right = LCA(root->right, p, q);

    if (LCA_left && LCA_right) {
        return root;
    }
    // either one of p,q is on one side OR p,q is not in L&R subtrees
    return LCA_left ? LCA_left : LCA_right;
}


void swap_int(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void swap_node(tree_node_t *a, tree_node_t *b)
{
    tree_node_t tmp = *a;
    *a = *b;
    *b = tmp;
}


int getHeight(tree_node_t *p) {
  int height = 0;
  while (p) {
    height++;
    p = p->parent;
  }
  return height;
}
 
// If we advance the deeper node dh steps above, both nodes would be at the same depth. 
// Then, we advance both nodes one level at a time. They would then eventually intersect 
// at one node, which is the LCA of both nodes. If not, one of the node would eventually 
// reach NULL (root’s parent), which we conclude that both nodes are not in the same tree. 
// However, that part of code shouldn’t be reached, since the problem statement assumed 
// that both nodes are in the same tree.

// As root->parent is NULL, we don't need to pass root in.
tree_node_t *LCA_parent_ptr(tree_node_t *p, tree_node_t *q) {
  int h1 = getHeight(p);
  int h2 = getHeight(q);
  // swap both nodes in case p is deeper than q.
  if (h1 > h2) {
    swap_int(&h1, &h2);
    swap_node(p, q);
  }
  // invariant: h1 <= h2.
  int dh = h2 - h1;
  for (int h = 0; h < dh; h++)
    q = q->parent;
  while (p && q) {
    if (p == q) return p;
    p = p->parent;
    q = q->parent;
  }
  return NULL;  // p and q are not in the same tree
}

int main()
{

    int i;
    int sample_data[] = {8,3,10,1,6,14,4,7,13};
    int len = sizeof(sample_data)/sizeof(sample_data[0]);
    tree_node_t *root = NULL;
    int *inorder_array = NULL;
    int *preorder_array = NULL;
    int *postorder_array = NULL;
    int array_len = 0;
    for (i = 0; i < len; i++) {
        root = insert(root, NULL, sample_data[i]);
    }
    // for (i = 0; i < 4; i++) {
    //     int index = rand() % len;
    //     root = delete(root, sample_data[index]);
    // }

    // if (isBST(root, INT_MIN, INT_MAX)) {
    //     printf("Valid BST\n");
    // } else {
    //     printf("Not a BST\n");
    // }

    // int ht = height(root);
    // printf("Height: %d\n", ht);

    // inorder_array = calloc(1, len*sizeof(int));
    // array_len = serialize_inorder(root, inorder_array);
    // inorder_array = (int *)realloc(inorder_array, array_len*sizeof(int));
    // preorder_array = calloc(1, array_len*sizeof(int));
    // postorder_array = calloc(1, array_len*sizeof(int));
    // serialize_preorder(root, preorder_array);
    // serialize_postorder(root, postorder_array);

    // post_index = array_len-1;
    // tree_node_t *new_tree = deserialize_postorder(inorder_array, postorder_array, 0, array_len-1);
    // if (compare(root, new_tree)) {
    //     printf("De-serialization works\n");
    // } else {
    //     printf("Nah, its broken\n");
    // }


    char *buffer = calloc(1, 256);
    serialize(root, buffer);
    int num_tokens = 0;
    char **tokens = tokenize(buffer, &num_tokens);
    //tree_node_t *new_root = deserialize(tokens, num_tokens);
    // if (compare(root, new_root)) {
    //     printf("De-serialization works\n");
    // } else {
    //     printf("Nah, its broken\n");
    // }
    int median = kth_samllest_element(root, 3);
    printf("Median: %d\n", median);

    dfs(root);
    printf("\n");
    level_order_traversal(root);
    tree_node_t *node = LCA(root, 13, 14);
    if (node) {
        printf("LCA: %d\n", node->value);
    }

    tree_node_t *p = search(root, 1);
    tree_node_t *q = search(root, 14);
    tree_node_t *ancestor = LCA_parent_ptr(p,q);
    if (ancestor) {
        printf("LCA: %d\n", ancestor->value);
    }
    return 0;
}
