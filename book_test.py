# كتاب البايثون
#  we can put a comma between string and integer as we do with variable
print("salma",100-25*3/4)

# True or False
print(10>5)
print("is it greater or equal?", 5>=-2)
print(f"is it greate or equal? {5>=-2}")

#  DECIMAL Library to solve this problem
print(0.1+0.2)

# the solution by using DECIMAL Library
from decimal import Decimal
x=Decimal("0.1")+Decimal("0.2")
print(x)

# %S يستخدم للتنسيق ويحول اي نوع بيانات ل string 
# f string احدث
name="salma"
age=23
my_hieght=160
my_weight=58
print("My name is %s, my age is %s"% (name,age))
print(" I love my name %s"% name)
print("if i add %d, %d, and %d, i get %d" % (age,my_hieght,my_weight, age+my_hieght+my_weight) )



