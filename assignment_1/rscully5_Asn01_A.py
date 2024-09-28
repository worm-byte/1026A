

'''
This code will output numbers in the Fibonacci Sequence
based on the range the user specifies.
'''

print("Project One (01) - Part A : Fibonacci Sequence")
#Input from user
#sequence_end will tell the program when to stop
sequence_end = int(input("Sequence ends at: "))

#new_num will be the newest value calculated in the sequence
new_num = 0

#prev_num1 will be the second most recent value calculated in the sequence
prev_num1 = 1

#prev_num2 will be the third most recent value calculated in the sequence
prev_num2 = 0

counter = 2

#If statement to filter 0 and 1 input first
if sequence_end < 0:
    print("Invalid entry.")
elif sequence_end == 0:
    print("0: 0 0")
elif sequence_end == 1:
    print("0: 0 0")
    print("1: 1 1")
else:
    #This will print if a number greater than 1 is entered
    print("0: 0 0")
    print("1: 1 1")
    #For loop that calculate and print all the numbers within range inputted at beginning
    for num in range(sequence_end-1):
        new_num = prev_num1 + prev_num2
        prev_num2 = prev_num1
        prev_num1 = new_num
        print(f"{counter}: {new_num} {new_num:,}")
        counter += 1

print("\nEND: Project One (01) - Part A")
print("Rosaline Scully rscully5 250966670")
