#===========================
c = "I Love Python\n" *42
print(c)
#===========================
age_in_mounth = 12*24
print(age_in_mounth, end="\n\n")
#===========================
age_in_years = int(age_in_mounth/12)
print(age_in_years)
#===========================
name = "Volodymyr"
my_age = "\nMy name is " + name + ", I'm "+str(age_in_years) + " year old\n"
print(my_age)
#===========================
a=1
b=2
c=a==b
print(c)
c=a>b
print(c)
c=a<b
print(c)
c=b>=a
print(c)
c=b<=a

print(c, end="\n\n")
#===========================
a = 2

b = 5

c = 6

d = str(a)+str(b)+str(c)
print(d)
results=type(d)
print(results)
#===========================