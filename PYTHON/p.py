import re
r = re.compile(r"""
      [a-zA-z0-9]+
      @
      [a-zA-z0-9]+
      (\.[a-z]{2,4})
""", re.VERBOSE)
m = r.search('My email is paiadithya26@gmail.com why')
print(m.groups())


#Three types of inheritance in pythons 

#Single inheritance  That is one parent and one child 

class  Parent:
    def __init__(self):
        print("Parent constructor")
    def show(self):
        print("Parent show method")
class Child(Parent):
    def __init__(self):
        print("Child constructor")
    def child(self):
        print("Child show method")
p = Parent()
p.show()
c = Child()
c.child()
c.show()


#multiple inheritance That is one parent and multiple childs

class Father :
    def __init__(self):
        print("Father constructor")
    def father(self):
        print("Father show method")
class Mother: 
      def __init__(self):
         print("Mother constructor")
      def mother(self):
         print("Mother show method")
class Child(Father,Mother):
      def __init__(self):
         print("Child constructor")
      def child(self):
         print("Child show method")
c = Child()
c.child()  #Child show method
c.father() #Father show method
c.mother() #Mother show method


#MultiLevel Inheritance

class GrandFather:
    def __init__(self):
        print("GrandFather constructor")
    def grandFather(self):
        print("GrandFather show method")
class Father(GrandFather):
      def __init__(self):
         print("Father constructor")
      def father(self):
         print("Father show method")
class grandSon(Father):
      def __init__(self):
         print("GrandSon constructor")
      def grandSon(self):
         print("GrandSon show method")
g = GrandFather()
g.grandFather()
f = Father()
f.father()
gson = grandSon()
gson.grandSon()



