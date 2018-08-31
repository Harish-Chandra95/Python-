print('Program to take list of nubers as input and return a tuple of first and last numbers in list')

# Getting Inputs from the User
numberList = input('Please enter your numbers list separated by a space: ')
# Iterating the input by and forming list
numberList = [str(number) for number in numberList.split(' ')]
print(numberList)


# Creating a new List which should contain list of Tuples
lenNumberList = []


# Iterating the Input list
for w in numberList:
    # Adding tuples  to the New List
    lenNumberList.append(tuple(w))

print(sorted(lenNumberList))

# Return first item and last item .
print(lenNumberList[0], lenNumberList[4])