#Ques1.

class Circle():
    def __init__(self,r):
        self.radius =r
    def getArea(self):
        return self.radius**2*3.14
    def getCircumference(self):
        return 2*self.radius*3.14
c=Circle(8)
print(c.getArea())
print(c.getCircumference())

#Ques2.

class Student():
    def __init__(self,name,rollno):
        self.n= name
        self.r= rollno
    def display(self):
        print("name is "+ self.n)
        print("rollno is "+ self.r)
s=Student("arti", str(7))
s.display()

#Ques3.

class Temperature():
    def __init__(self,far,cel):
        self.f=far
        self.c=cel
    def convertFarenhiet(self):
        farenheit=9/5*(self.c)+32
        print(farenheit)
    def convertCelsius(self):
        celsius=((self.f)-32)*(5/9)
        print(celsius)
p=Temperature(0,68)
p.convertFarenhiet()
p.convertCelsius()

#Ques4.

class Moviedetails():
    def __init__(self,Moviename,artistname,yearofrelease,rating):
        self.m=Moviename
        self.a=artistname
        self.y=yearofrelease
        self.r=rating
    def display(self):
        print("movie name is "+self.m)
        print("artist name is "+self.a)
        print("year of release "+self.y)
        print("rating is "+self.r)

    def update(self,moviename,artistname,yearofrelease,rating):
        self.q=moviename
        self.w=artistname
        self.e=yearofrelease
        self.t=rating
        print("movie name is "+self.q)
        print("artist name is "+self.w)
        print("year of release "+self.e)
        print("reting is "+self.t)
z=Moviedetails("race","salman",str(2018),str(4))
z.display()
z.update("RACE","SAIF ALI KHAN",str(2008),str(4))

#Ques5.

class Expenditure():
    expenditure=5000
    savings=1
    def __init__(self):
        print(self.expenditure)
        print(self.savings)
    def display(self):
        print(self.expenditure)
        print(self.savings)
        salary=50001
        totalsalary=(self.expenditure)+(self.savings)
        print(salary)
        print(totalsalary)
z=Expenditure()
z.display()


