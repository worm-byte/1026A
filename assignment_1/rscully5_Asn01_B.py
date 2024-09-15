'''
CS1026a 2023
Assignment 01 Project 01 - Part B
Rosaline Scully
250966670
rscully5
October 2, 2023
'''

'''
This code will output all of the prime numbers
within a range stipulated by the user.
'''

print("Part One - Project B: Prime Choice\n")

#Input range of numbers from user

#start_num is the beginning of the range
start_num = int(input("Prime Numbers starting with: "))

#q2 is the end of the range
q2 = int(input("and ending with: "))

#end_num is a second variable to hold end of range value in case numbers are entered backwards
end_num = q2

#Test for negative numbers
if start_num < 0 or end_num < 0:
    print("Negative numbers cannot be prime numbers. Please input a valid number.\n")
#Output if the first number is 0 (which is not a prime)
elif start_num == 0:
    print("\nPrime numbers in the range from:", start_num, "and", end_num, "are:")
    #for loop that will loop through all the numbers from start_num to end_num and check if they are prime
    #first for loop will go through the range of numbers
    for n in range(start_num + 2, end_num + 1):
        #prime_check is a boolean variable that will change to False if a composite number is detected
        prime_check = True
        #second for loop will go through all numbers from 2 until n to see if n is divisible by any of them.
        for x in range(2, n):
            if n % x == 0:
                prime_check = False
        #if statement that will print prime numbers found
        if prime_check:
            print(n, "is prime")
#Output if the first number is 1 (which is not a prime number)
elif start_num == 1:
    print("\nPrime numbers in the range from:", start_num, "and", end_num, "are:")
    for n in range(start_num + 1, end_num + 1):
        prime_check = True
        for x in range(2, n):
            if n % x == 0:
                prime_check = False
        if prime_check:
            print(n, "is prime")
#Output if the person enters the numbers in backwards
elif start_num > q2:
    end_num = start_num
    start_num = q2
    print("\nIncorrect Input:",end_num,"is greater than",start_num)
    print("The numbers have been automatically switched.\n")
    print("Prime numbers in the range from:",start_num,"and",end_num,"are:")
    #I'm still checking if they entered 0 or 1 here
    if start_num == 0:
        for n in range(start_num + 2, end_num + 1):
            prime_check = True
            for x in range(2, n):
                if n % x == 0:
                    prime_check = False
            if prime_check:
                print(n, "is prime")
    elif start_num == 1:
        for n in range(start_num + 1, end_num + 1):
            prime_check = True
            for x in range(2, n):
                if n % x == 0:
                    prime_check = False
            if prime_check:
                print(n, "is prime")
    else:
        #This will be executed if numbers greater than 1 are entered
        for n in range(start_num,end_num+1):
            prime_check = True
            for x in range(2,n):
                if n % x == 0:
                    prime_check = False
            if prime_check:
                print(n,"is prime")
else:
    #Final execution if numbers greater than 1 are entered correctly
    print("\nPrime numbers in the range from:",start_num,"and",end_num,"are:")
    for n in range(start_num,end_num+1):
        prime_check = True
        for x in range(2,n):
            if n % x == 0:
                prime_check = False
        if prime_check:
            print(n,"is prime")
print("\nEND: Project One (01) - Part B")
print("Rosaline Scully rscully5 250966670")



