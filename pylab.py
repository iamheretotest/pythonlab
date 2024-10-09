#1 Program to check whether the given number is prime or not

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")
else:
    print("The number is not prime")            


#2 Function to calculate length and check for palindrome

count = 0
i=0
strn = input("enter: ")
while i<len(strn):
    count+=1
    i+=1
rev = strn[::-1]
print("Length of the string is",count)
if strn == rev :
    print("Palindrome!")
else:
    print("Not a Palindrome!") 
           

#3 Python function to print number of words in a sentence

def WordCount():
    strn = input("Enter a sentence: ")
    strn = strn.split()
    count = 0
    i = 0
    while i<len(strn):
        count+=1
        i+=1
    print("Number of words in the sentence are",count)
WordCount()    

# Alternative
def WordCount():
    strn = input("Enter a sentence: ")
    strn = strn.split()
    print("Number of words in the sentence are",len(strn))
WordCount()

#4 Take numbers as input and find sum and average of it

L = []
while True:
    lst = int(input("Enter the numbers(type 0 to stop): "))
    if lst == 0:
        break
    L.append(lst)

if L:  # Same as if len(L)>0:
    print("Sum of all the elements in the list is", sum(L))
    print("Average of all the elements present in the list is", sum(L) / len(L))
else:
    print("Sum and Average both are 0")


#5 Copying odd lines of a files to another file

ipfile = open(r"F:\python\input.txt",'r')
lines = ipfile.readlines()
ipfile.close()

oddLines = lines[::2]

opfile = open(r"F:\python\output.txt",'w')
for l in oddLines:
    opfile.write(l)
opfile.close()    
print("Content Printed into another file!")


6 Read names and ph no.s and store it in a dict providing the option of fetching back

D={}
NumberOfPersons = int(input("Enter number of persons: "))
for i in range(NumberOfPersons):
    name = input("Enter your name: ")
    ph_number = input("Enter your ph number: ")
    D[name]=ph_number
print(D)    

fetch = input("Enter the name for fetching ph number: ")
if fetch in D :
    print(D[fetch])
else:
    print("Entry doesn't exist!")    


#7 Function to check whether a number is even or odd

def check(num):
    if num%2==0 :
        print(f"{num} is an even number!")
    else:
        print(f"{num} is a odd number!") 

num = int(input("Enter the number: "))           
check(num)


#8 Program to count the occurences of the characters in a string

D = {}
strn = input("Enter here: ")
for ch in strn :
    D[ch] = D.get(ch,0) + 1
print(D)
