def exclusive_array_product(array):
    product_array = [0]*(len(array) + 1)
    product_array[0] = 1
    product = 1

    for i in xrange(1, len(array)+1):
        product_array[i] = product
        product *= array[i-1]
    print product_array
    product = 1
    for i in xrange(len(array), 0, -1):
        product_array[i] *= product
        product *= array[i-1]
    print product_array

exclusive_array_product([1,2,3,4,5])



