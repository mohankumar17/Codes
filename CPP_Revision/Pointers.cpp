#include<stdio.h>
int main()
{
  int x=100;
  double y=12;
  int *p=&x;
  double *q=&y;
  printf("x and y : %d %d",sizeof(p),sizeof(q));
  return 0;
}
