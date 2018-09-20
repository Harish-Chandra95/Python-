s = input("enter the string")
s1 = list(s.replace(" ","")) #converting the input into list and removing spaces between them
print(s1)

individual=[] #every individual character passed in the string
repeated=[] #every repeated characcter passeed in the string
unique=[] #characters whose count is 1 in the string

for c in s1:
    if c not in individual:
        individual.append(c) #append each character in the string
    else:
         repeated.append(c)  #append repeated characters into this list

for d in s1:
    if d in individual and d not in repeated:
        unique.append(d)

#prints the first non-repeated character
print("The first non-repeated character in the string is: ", unique[0])

