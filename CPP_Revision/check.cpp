#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
  int a[10]={4,3,7,6,9,2,1,5,11,12};
  int n=sizeof(a)/sizeof(a[0]);
  //sort(a,a+n);
  /*int pos,num;
  cin>>pos>>num;
  if(pos<=0 || pos>n)
  {
    cout<<"Invalid Position";
  }
  else{
    for(int i=n-1;i>=pos;i--)
    {
       a[i]=a[i-1];
    }
    a[pos-1]=num;
  }*/
  int pos;
  cin>>pos;

  for(int i=pos;i<n;i++)
  {
      a[i]=a[i+1];
  }

  for(int i=0;i<n-1;i++)
  {
     cout<<a[i]<<" ";
  }

  return 0;
}
