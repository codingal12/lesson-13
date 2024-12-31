###Write a program to check how many times a character is repeated in a word?

word=str(input("enter your word"))
charecter=str(input("enter the charecter to chek"))

i=0
c=0
while len(word)>i:
    if word[i]==charecter:
        c=c+1

    i=i+1
print("the charecter you have given it appered",c)