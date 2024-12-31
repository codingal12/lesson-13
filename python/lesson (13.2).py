#Write a program to demonstrate a Floyd triangle pattern?

rows=int(input("enter the row count"))
number=1

for x in range(1,rows+1):
    for y in range(1,x+1):
          print(number,end="  ")
          number=number+1
    print()