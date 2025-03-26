#This file is for practicing the TypeCasting in Python
#This will be fun so lets get started.

name = "Abhishek "
age = 29
GPA = 1.6
Student = False
Employed = False

print(type(name))
print(type(age))
print(type(GPA))
print(type(Student))
print(type(Employed))

#Explicit Typecasting
# It is manually converting the data type of an object to the required data type

age = float(age)
GPA = int(GPA)
Student = str(Student)
Employed = str(Employed)

print(type(age))
print(type(GPA))


#implicit Typecasting
# It is automatically converting the data type of an object to the required data type

aa = 2
yy = 3.5

zz = aa + yy
print(zz)   # This will print 5.5

# This is the end of the TypeCasting file