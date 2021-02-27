#CLASS AND OBJECT
'''
#DATA ABSTRACTION AND DATA ENCAPSULATION
class A:
    def __init__(self,val):
        print('A constructor')
        self.x=val  #public
        self.__y=val  #private
    def disp(self):
        print(self.x,self.__y)
    def set(self):
        self.__y=10

ob=A(20)
ob.disp()

ob.x=10  #will be allocated because x is public
ob.__y=10  #will not be allocated because y is private
ob.disp()

ob.set()
ob.disp()
#print(A.x)
#print(ob.__y)
'''

#INHERITANCE AND POLYMORPHISM
'''class A:
    def __init__(self,val):
        print('A constructor')
        self.x=val
    def disp(self):
        print(self.x)

class B(A):
    def __init__(self,val):
        #super().__init__  #automatically gets initialized
        print('B constructor')
        self.y=val
    def disp(self):
        print(self.y)

ob1=A(10)
ob2=B(20)
ob2.disp()'''


#FUNCTION OVERLOADING
'''def disp(a,b=None):
    if b==None:
        print(a)
    else:
        print(a,b)

disp(1,3)
disp(2)
'''
#OBJECT OVERLOADING

class A:
    def __init__(self,val):
        self.x=val
    def disp(self):
        print(self.x)
    def __add__(self,t):
        self.x=self.x+t.x

ob1=A(10)
ob2=A(20)
ob1.disp()
ob2.disp()

ob1+ob2   #ob1 will be changed
ob1.disp()

ob2+ob1   #ob2 will be changed
ob2.disp()
