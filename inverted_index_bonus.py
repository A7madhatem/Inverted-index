# بسم الله الرحمن الرحيم
# صل علي النبي 

fileNames = ["doc1.txt", "doc2.txt", "doc3.txt", "doc4.txt", "doc5.txt",
            "doc6.txt", "doc7.txt", "doc8.txt", "doc9.txt", "doc10.txt"]

stopWords = ['a', 'an', 'and', 'as', 'at', 'be', 'for', 'from', 'has', 
            'he', 'in', 'is', 'it', 'of', 'on', 'that', 'the', 'to', 'was', 'with','this']

# Remove stop words from each document
for fileName in fileNames:
    with open(fileName, "r") as file:
        text = file.read()
        words = text.split()
        filteredWords = [word for word in words if word.lower() not in stopWords]
        cleanedText = ' '.join(filteredWords)
        
    # Write the cleaned text back to the same file
    with open(fileName, "w") as file:
        file.write(cleanedText)

# Open the new cleanded files and take one word input from the user
word = input("Enter the word here : ")
for i in range(len(fileNames)):
    with open(fileNames[i], "r") as file:
        text = file.read()
        words = text.split()
        
    # Search for the word in the documents and print its index if found
    if word in words:
        print("[", i+1, "]", end=" ")