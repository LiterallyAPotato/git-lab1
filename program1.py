import sys
'''
Program takes a string of the format $X.YZ 
and outputs the number of dollars, quarters, dimes, nickels, 
and pennies which exist. Always uses the least number of 
possible coins and bills.

https://ncssm.instructure.com/courses/8915/assignments/209936
'''

'''
format the string like this in VSCode:
"$""9.87"

by putting two quotes between the dollar sign and the amount
'''

#check for correct number of arguments
if (len(sys.argv) > 2):
    print("ERROR: Too many arguments given")
    sys.exit(-1)
if (len(sys.argv) == 1):
    print("ERROR: No argument given")
    sys.exit(-1)

amount = sys.argv[1]

#check that formatting is correct
dollarCount = amount.count("$")
if dollarCount == 0 or amount[0] != "$":
    print("ERROR: The string must being with $")
    exit(-1)
if dollarCount > 1:
    print("ERROR: Too many $")
    exit(-2)
dotCount = amount.count(".")
if dotCount == 0:
    print("ERROR: The string must being with $")
    exit(-3)
if dotCount > 1:
    print('ERROR: The string has too many "."')
    exit(-4)
try:
    cents = int(amount[-2:])
except Exception:
    print("ERROR: String must include cents amount")
    exit(-5)
try:
    dollars = int(amount[1:-3])
except Exception:
    print("ERROR: String must include dollar amount")
    exit(-6)
if amount[-3] != ".":
    print('ERROR: There must be a "."')
    exit(-7)


cost = 987
values = [100, 25, 10, 5]
units = ["dollar", "quarter", "dime", "nickel"]
#plural of penny is pennies
#edge case, handle them separately

for x in range(len(values)):
    curr = values[x]
    counter = 0
    while cost > curr:
        cost -= curr
        counter += 1
    #subtract as many of value as you can
    #once you can't, move on to the next value
        
    if counter == 1:
        print(1, units[x])
    else:
        print(counter, units[x]+"s")

if cost == 1:
    print("1 penny")
else:
    print(cost, "pennies")


