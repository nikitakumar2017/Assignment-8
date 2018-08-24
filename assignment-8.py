#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
import math
class circle:
    def __init__ (self,r):
        self.radius=r
    def getArea(self):
        self.area=math.pi*(self.radius**2)
        return self.area
    def getCircumference(self):
        self.c=2*math.pi*self.radius
        return self.c
r=int(input("Enter radius of circle "))
c1=circle(r)
print("Area of circle is:",c1.getArea(),"and circumference is:",c1.getCircumference())

#Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
#1. Display - It should display all informations of the student. 
#2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.
class student:
    __name=''
    __rollno=0
    __age=0
    __marks=0
    def __init__(self,name,rno):
        self.__name=name
        self.__rollno=rno
    def setAge(self,age):
        self.__age=age
    def setMarks(self,marks):
        self.__marks=marks
    def display(self):
        print("Name:",self.__name,"\nRollno:",self.__rollno,"\nAge:",self.__age,"\nMarks:",self.__marks)

name=input("Enter name ")
rno=int(input("Enter rollno "))
s1=student(name,rno)
age=int(input("Enter the age of student "))
s1.setAge(age)
marks=int(input("Enter marks of student "))
s1.setMarks(marks)
s1.display() 

#Q.3- Create a Temprature class and create two methods: 
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temperature:
    def convertFahrenheit(self,c):
        f=((c*9)/5)+32
        return f
    def convertCelsius(self,f):
        c=(f-32)/1.8
        return c
t=Temperature()
tempc=int(input("Enter temperature in Celcius "))
tempf=int(input("Enter temperature in Fahrenheit "))
print(tempc,"in Fahrenheit is",t.convertFahrenheit(tempc),"and",tempf,"in Celclius is",t.convertCelsius(tempf)) 

#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details.
class MovieDetails:
    __artistname=''
    __yearofrelease=0
    __rating=0
    def add(self,name,year,rating):
        self.__artistname=name
        self.__yearofrelease=year
        self.__rating=rating
    def display(self):
        print("Artist Name: ",self.__artistname,"\nYear of release:",self.__yearofrelease,"\nRating:",self.__rating)
    
m=MovieDetails()
name=input("Enter name of artist ")
year=int(input("Enter year of release "))
rating=int(input("Enter rating "))
m.add(name,year,rating)
m.display()

#Q.5- Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
    def animal_attribute(self,attr):
        print("My attribute is:",attr)
class Tiger(Animal):
    pass
t=Tiger()
t.animal_attribute("I am a cat") 

#Q.6- What will be the output of following code.
'''The output will be
'A' 'B'
'A' 'B'
because a.f() calls function f() which calls g() which returns 'A' and b.f() calls f() which calls self.g() so this means g() of class B will be called.
a.g() and b.g() will call g() of class A and B respectively. Here, method overriding is done. '''

#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.
class shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        self.area=self.length*self.breadth
        return self.area
class rect(shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
class square(shape):
    def __init__(self,s):
        self.length=s
        self.breadth=s
    pass
r=rect(10,2)
s=square(5)
print("Area of rectangle:",r.area(),"and area of square:",s.area())
