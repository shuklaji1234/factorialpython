# Python program to find the factorial of a number provided by the user.

# function to print factorial of given number

def isOddEven(number):
   factorial = 1
   if number < 0:
      print("Sorry, factorial does not exist for negative numbers")
   elif number == 0:
      print("The factorial of 0 is 1")
   else:
      for i in range(1,number + 1):
          factorial = factorial*i
      print("The factorial of",number,"is",factorial) 

# change the value for a different result
num = int(input("Enter a number: "))

isOddEven(num)
