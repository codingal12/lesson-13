###Write a program to find the sum of natural numbers.
n=int(input("enter your number"))

x=1
sum=0
while x<=n:
    sum=sum+x
    x=x+1
    print(sum)
print("the sum is",sum)