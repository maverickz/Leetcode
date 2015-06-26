#include <iostream>

using namespace std;

bool v[10];
int main(void) {
  long non_self = 0;
  for(long i = 1; i < 10; ++i) {
    if(!(v[i])) std::cout << i << '\n';
    non_self = i + (i%10) + (i/10)%10 + (i/100)%10 + (i/1000)%10 + (i/10000)%10 +(i/100000)%10;
    v[non_self] = 1;
  }
  return 0;
}