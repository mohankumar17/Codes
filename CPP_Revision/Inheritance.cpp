#include<iostream>
#include<bits/stdc++.h>
using namespace std;

class A{
public:
  int val;
  int getDetails(){
    return val;
  }

};
int getDetails()::A{

}
class B:public A{
public:
};

int main()
{
  B ob_B;
  ob_B.val=20;
  cout<<ob_B.getDetails();

  return 0;
}
