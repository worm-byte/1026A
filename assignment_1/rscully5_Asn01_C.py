'''
CS1026a 2023
Assignment 01 Project 01 - Part C
Rosaline Scully
250966670
rscully5
October 2, 2023
'''

'''
This code will display the rate of increase 
of computing power based on input from the user 
like starting number of transistors, starting year,
and total number of years.
'''
print("Project One (01) - Part C: The Moore the Merrier")

#start_num is an integer variable that holds the starting number of transistors.
start_num = int(input("Starting Number of transistors: "))

#start_year holds the starting year.
start_year = int(input("Starting Year: "))

#total_years holds the total number of years the program will run for.
total_years = int(input("Total Number of Years: "))

#final_year will tell the program what year to stop at.
final_year = start_year + total_years

#This function will round and format the 3rd column of the output
def decimal_format():
    if formatted_flops[1] == ".":
        #newflop turns formatted_flops from an int into a float so that it can be rounded properly
        newflop = float(formatted_flops[0:5])
        round(newflop,2)
        return "{0:.2f}".format(newflop)
    elif formatted_flops[2] == ".":
        newflop = float(formatted_flops[0:6])
        round(newflop,2)
        return "{0:.2f}".format(newflop)
    elif formatted_flops[3] == ".":
        newflop = float(formatted_flops[0:7])
        round(newflop,2)
        return "{0:.2f}".format(newflop)


print("\nYEAR : TRANSISTORS : FLOPS:")
#This for loop will output each line of code until the desired number of years.
for n in range(start_year, (final_year + 1), 2):
    #flops calulates the number of flops based on start_num
    flops = start_num * 50
    #This if statement will print different outputs depending on the number of flops
    if flops < 1000:
        print(n, " ", end="")
        print(f"{start_num:,} ", end="")
        print("{:.2f}".format(flops), "FLOPS", flops)
    elif 1000 <= flops < 1000000:
        print(n, " ", end="")
        print(f"{start_num:,} ", end="")
        #formatted_flops replaces all ',' with '.' within the number
        formatted_flops = "{:,}".format(flops).replace(",", ".")
        print(decimal_format(), "kiloFLOPS", f"{flops:,}")
    elif 1000000 <= flops < 1000000000:
        print(n, " ", end="")
        print(f"{start_num:,} ", end="")
        formatted_flops = "{:,}".format(flops).replace(",", ".")
        print(decimal_format(), "megaFLOPS", f"{flops:,}")
    elif 1000000000 <= flops < 1000000000000:
        print(n, " ", end="")
        print(f"{start_num:,} ", end="")
        formatted_flops = "{:,}".format(flops).replace(",", ".")
        print(decimal_format(), "gigaFLOPS", f"{flops:,}")
    elif 1000000000000 <= flops < 1000000000000000:
        print(n, " ", end="")
        print(f"{start_num:,} ", end="")
        formatted_flops = "{:,}".format(flops).replace(",", ".")
        print(decimal_format(), "teraFLOPS", f"{flops:,}")
    elif 1000000000000000 <= flops < 1000000000000000000:
        print(n, " ", end="")
        print(f"{start_num:,} ", end="")
        formatted_flops = "{:,}".format(flops).replace(",", ".")
        print(decimal_format(), "petaFLOPS", f"{flops:,}")
    elif 1000000000000000000 <= flops < 1000000000000000000000:
        print(n, " ", end="")
        print(f"{start_num:,} ", end="")
        formatted_flops = "{:,}".format(flops).replace(",", ".")
        print(decimal_format(), "exaFLOPS", f"{flops:,}")
    elif 1000000000000000000000 <= flops < 1000000000000000000000000:
        print(n, " ", end="")
        print(f"{start_num:,} ", end="")
        formatted_flops = "{:,}".format(flops).replace(",", ".")
        print(decimal_format(), "zettaFLOPS", f"{flops:,}")
    start_num = start_num * 2

print("\nEND: Project One (01) - Part C")
print("Rosaline Scully rscully5 250966670")








