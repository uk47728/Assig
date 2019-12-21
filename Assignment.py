#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q 1: 
Ans: Python is an object-oriented programming language. It allows us to develop applications using an Object Oriented 
     approach. In Python, we can easily create and use classes and objects.

     Major principles of object-oriented programming system are given below.

     Object.
     Class.
     Method.
     Inheritance.
     Polymorphism.
     Data Abstraction.
     Encapsulation.

Q 2: 
Ans: 1. Modularity for easier troubleshooting.
     2. Reuse of code through inheritance.
     3. Flexibility through polymorphism.
     4. Effective problem solving.

Q 3:
Ans: Python method is called on an object, unlike a function. ... Since we call a method on an object, it can access the
     data within it. A method may alter an object's state, but Python function usually only operates on it,and then
     prints something or returns a value.

Q 4:
Ans: Class:
	   A class is a virtual entity and can be seen as a blueprint of an object.
     i.e:
	 class Employee:  
         id = 10;  
         name = "usama"  
         def display (self):  
         print(self.id,self.name)  

     Object:
	    The object is the instance of a class. The process of creating an object can be called as instantiation.
     i.e:
	 <object-name> = <class-name>(<arguments>) 

     Attribute:
	        Class attributes belong to the class itself they will be shared by all the instances. Such attributes are
     defined in the class body parts usually at the top, for legibility. Unlike class attributes, instance attributes 
     are not shared by objects.
     i.e:
	 class sampleclass: 
     count = 0     # class attribute 
  
     def increase(self): 
        sampleclass.count += 1
  
     # Calling increase() on an object 
     s1 = sampleclass() 
     s1.increase()         
     print s1.count 
  
     # Calling increase on one more 
     # object 
     s2 = sampleclass() 
     s2.increase() 
     print s2.count 
  
     print sampleclass.count 

     Behavior:
	      Attributes are the characteristics of the class that help to distinguish it from other classes. Behaviors are the tasks that an object performs.
     A person's attributes, for example, include their age, name, and height,
     while their behaviors include the fact that a person can speak, run, walk, and eat.
	      
Q 5:
Ans:
	class Car:  
    model = "prosmatic" 
    color ="Black"
    name = "Civic"  
         def display1 (self):  
        print(self.name)  
         def display2 (self):  
        print(self.madel)  
         def display3 (self):  
        print("self.color)  
ob1 = Car() 
ob2 = Car()
ob3 = Car()
ob4 = Car()
ob5 = Car()
ob1.display1() 
ob1.display2()
ob1.display3()
ob2.display1() 
ob2.display2()
ob2.display3()
ob3.display1() 
ob3.display2()
ob3.display3()
ob4.display1()
ob4.display2() 
ob4.display3() 
ob5.display1() 
ob5.display2() 
ob5.display3() 


     


# In[ ]:




