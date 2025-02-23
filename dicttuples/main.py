# Tuple is immutable, very handy while packing, unpacking and zipping
def find_pe_and_pb(price:float,eps:float,bv:float) -> tuple[float,float]:
    '''
    Function to find Price to Earning and Price to Book Value Ratio. Notice the tuple implementation.
    :param price: Current price of a stock
    :param eps: Earning per share
    :param bv: Book Value of the share
    :return: returns packed tuple of two float values
    '''
    pe = price/eps
    pb = price/bv
    return pe,pb # comma-separated return values are interpreted as tuples

#Useage find_pe_and_pb
pe_ratio, pb_ratio = find_pe_and_pb(120,80,50) # Unpacking
print(f'Pe_Ratio: {pe_ratio}')
print(f'Pb_Ratio: {pb_ratio}')


x:float = float(input("Enter an Integer\n"))
if x%2 == 0:
    print("It is even")
else:
    print("It is odd")

# Ternary Operator
print("Even" if x%2==0 else  "Not Even\n" if type(x) == int else "Wrong Input\n")

# *args and **kwargs parameter type
def even(*args) -> list[str]:
    '''
    :param args: input a sequence of numbers (Create Tuple)
    :return: boolean value
    '''
    ct = []
    for arg in args:
        if arg%2 == 0:
            ct.append("Yes")
        else:
            ct.append("No")
    return ct
print(even(1,656,48,1,92,6))



def keyval(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} has a {value}")

keyval(Rana = "Car", Pranay ="Bike", Wrick = "Football")

# Write a lamda function for identification of even-odd
evenodd = lambda x : "Even" if x%2 == 0 else "Odd" if type(x) == int else "Wrong Input\n"
print(evenodd(2))
print(evenodd(5))
print(evenodd(2.5))


#Writing a function to find total expense
def expense_cal(expenses:list[float])-> float:
    '''
    :param expenses: Input list containg expenses
    :return:Returns total expenses from the list of expenses
    '''
    count = 0
    for expense in expenses:
        count += expense
    return count

print(help(expense_cal))

ram_expenses = [10, 15 , 20 , 35]
jam_expenses = [12, 35 , 28 , 15]



print(f'Total Expense of Ram:{expense_cal(ram_expenses)}')
print(f'Total Expense of Ram:{expense_cal(jam_expenses)}')

total_ram = 0
for expense in ram_expenses:
        total_ram = total_ram + expense
print(f'Total Expense of Ram:{total_ram}')

total_jam = 0
for expense in jam_expenses:
        total_jam1 = total_jam1 + expense

print(f'Total Expense of Jam:{total_jam}') #Okay

# Comment Added








