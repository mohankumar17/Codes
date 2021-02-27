#include<iostream>
//#include<bits/stdc++.h>
using namespace std;
class A{
public:
virtual void func()=0;
};

class B:public A{
public:
  void func()
  {
    cout<<"Child class"<<endl;
  }

};


int main()
{
 A *p;
 B ob;
 p=&ob;
p->func();
  return 0;
}
