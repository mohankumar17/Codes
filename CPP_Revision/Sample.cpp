#include<iostream>
#include<bits/stdc++.h>
using namespace std;

class Student{
  string name;
  int id;
  int marks;
public:
  Student(string name,int id,int marks)
  {
    this->name=name;
    this->id=id;
    this->marks=marks;
  }

  void getDetails()
  {
    cout<<endl;
    cout<<"Name : "<<this->name<<endl;
    cout<<"ID : "<<this->id<<endl;
    cout<<"Marks : "<<this->marks<<endl;
  }

  bool result()
  {
    if(this->marks>50)
    return true;
    else
    return false;
  }
};

int main()
{

  string name;
  int id,marks;
  cout<<"Enter Name : ";
  cin>>name;
  cout<<"\nEnter ID : ";
  cin>>id;
  cout<<"\nEnter Marks : ";
  cin>>marks;

  Student s(name,id,marks);
  s.getDetails();

  bool b=s.result();
  if(b==1)
  cout<<"Pass";
  else
  cout<<"Fail";

  return 0;
}
