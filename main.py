# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:Shashvat Nilesh Kawali
# Date:30 january 2029

print("--- Factorial Finder ---\n")


# Write your code here
n=int(input("Enter Number:"))
factorial=1
if(n>=0):
    for i in range(1,n+1):
        factorial=factorial*i
    print(f"Factorial of {n} is {factorial}")
else:
    print(f"Factorial of 13 is Not Defined")

