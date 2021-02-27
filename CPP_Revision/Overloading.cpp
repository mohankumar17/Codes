#include<iostream>
//#include<bits/stdc++.h>
using namespace std;
class A{
public:
  void func(int x)
  {
    cout<<"int:"<<x<<endl;
  }

  void func(double x)
  {
    cout<<"double:"<<x<<endl;
  }

  void func(string x)
  {
    cout<<"string:"<<x;
  }

};
int main()
{
  A ob;
  ob.func(10);
  ob.func(7.5);
  ob.func("Mohan");
  return 0;
}
