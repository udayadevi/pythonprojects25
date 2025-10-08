#program to caluculate avergae height form a list of heights
heights=list(map(int,input("enter all heights separated bya  space").split()))
add=0
c=0
for i in range(len(heights)):
    add+=heights[i]
    c+=1
average=(add)//c
print(average)


