import csv

def count_words(inputFile):
    #It itereates through each line of the input file.
    #If the word is less than 3, it goes to the file small-words.txt
    #If the word is 3 or more charactes, it goes to the file large-words.txt
    largeWords = []
    smallWords = []
    #Reading
    with open(inputFile, mode='r') as inputFile:
        while True:
            line = inputFile.readline()
            words = line.split()
            for word in words:
                if len(word) >= 3:
                    largeWords.append(word)
                else:
                    smallWords.append(word)

            if not line:
                break
        largeWords = set(largeWords)
        smallWords = set(smallWords)
    #Writing
    with open("large-words.txt", "w") as largeWordsFile:
        for word in largeWords:
            largeWordsFile.writelines(word+ "\n")
    
    with open("small-words.txt", "w") as smallWordsFile:
        for word in smallWords:
            smallWordsFile.writelines(word +"\n")

    return len(largeWords)+len(smallWords)

def ex3():
    total_words = count_words("files/words.txt")
    print(f"Total words: {total_words}.")

ex3()