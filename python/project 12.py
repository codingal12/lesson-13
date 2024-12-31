## this is a project
num=float(input("enter a decimal number"))
binary=""
while num>0:
    y=num%2
    binary=y+binary
    num//=2
print(binary)