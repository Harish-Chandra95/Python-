word = []
with open("E:\\file1.txt") as f1:
        for line in f1:
            word.append(line.split(" "))  #The first file is converted into list
        print("The list of words in file1 are : ", word[0])

word2 = []
with open("E:\\file2.txt") as f2:
        for lines in f2:
            word2.append(lines.split(" "))   #the second file is converetd into list here
        print("The list of words in file2 are: ", word2[0])

difference = []
for i in word[0]:
        if i not in word2[0]:   #difference of words in file1 and file2
            difference.append(i)  #append the remaining words to the list

wf1=difference
print("The words of file1 without the the words of file2 are: ",wf1)

wf2= ' '.join(wf1)  #converting the words in list to string using join function
print("The string of file1 without the words of file2 is: ",wf2)

