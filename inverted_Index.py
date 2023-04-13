# بسم الله الرحمن الرحيم
# صل علي النبي 

fileNames = ["doc1.txt", "doc2.txt", "doc3.txt", "doc4.txt", "doc5.txt", 
            "doc6.txt", "doc7.txt", "doc8.txt", "doc9.txt", "doc10.txt"]
texts = []

# Read files 
for fileName in fileNames:
    with open(fileName, "r") as file:
        texts.append((file.read()).split())

# Find the word in the files
word = input("Enter the word here : ")
for i in range(len(texts)):
    for j in range(len(texts[i])):
        if word == texts[i][j]:
            print("[",i+1,"]",end=" ")
            break