#include<iostream>
using namespace std;
int main()
{
  int ar[]={3,5,2,8,9};
  int *p=ar;
  cout<<ar<<endl;
  cout<<*ar<<endl;
  cout<<ar+1<<endl;
  cout<<*(ar+1);
  /*for(int i=0;i<5;i++)
  {
    //cout<<*(p+i)<<" ";
    cout<<ar+i<<" ";
  }
  //cout<<endl;
  /*int ar2[3][2]={1,2,3,4,5,6};
  int (*p)[2]=ar2;
  for(int i=0;i<3;i++)
  {
    for(int j=0;j<2;j++)
    {
      //cout<<*(*(ar2+i)+j)<<" ";
      cout<<*(*(p+i)+j)<<" ";
    }
    cout<<endl;
  }*/

  return 0;
}
