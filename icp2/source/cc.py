fname = input("Enter file name: ")

num_words = 0
num_char = 0

with open(fname, 'r') as f: #In python the with keyword is used when working with unmanaged resources (like file streams).
    for line in f:#here we  read the complete file
        words = line.split(" ")
        num_words += len(words)
print("Number of words:")
print(num_words)
f.close()


with open(fname, 'r') as f:
    ch1= f.readline()
    for line in ch1:
        #now the  line will be read
        char = list(ch1)
        num_char += len(char)
        ch1 = f.readline()
print("Number of charaters:")
print(num_char)