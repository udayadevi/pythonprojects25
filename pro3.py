#add digits of  anumber
num=int(input("enter a  number"))
s=0
while num>0:
    r=num%10
    s+=r
    num=num//10
print(s)