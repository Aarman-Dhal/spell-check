# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    options = "Main Menu \n 1: Spell Check a Word (Linear Search) \n 2: Spell Check a Word (Binary Search) \n 3: Spell Check Alice In Wonderland (Linear Search) \n 4: Spell Check Alice In Wonderland (Binary Search) \n 5: Exit"
    print("\n" + options)

    user_selection = input("Enter menu selection (1-5): ")
    
    while user_selection != '5':
        if user_selection == '1':
            searched_word = input("Please enter a word: ").lower()
            start_time = time.time()
            pos = (linearSearch(dictionary, searched_word))
            print("Linear Search starting...")
   
            if pos != -1:
                time_elapsed = time.time() - start_time
                print(searched_word + " is IN the dictionary at position " + str(pos) + ". (" + str(time_elapsed) + " seconds)")
                print("\n" + options)
                user_selection = input("Enter menu selection (1-5): ")
            else:
                time_elapsed = time.time() - start_time
                print(searched_word + " is NOT IN the dictionary. (" + str(time_elapsed) + " seconds)")
                print("\n" + options)
                user_selection = input("Enter menu selection (1-5): ")

        elif user_selection == '2':
            searched_word = input("Please enter a word: ").lower()
            start_time = time.time()
            pos = binarySearch(dictionary, searched_word)
            print("Binary Search starting...")
    
            if pos != -1:
                time_elapsed = time.time() - start_time
                print(searched_word + " is IN the dictionary at position " + str(pos) + ". (" + str(time_elapsed) + " seconds)")
                print("\n" + options)
                user_selection = input("Enter menu selection (1-5): ")
            else:
                time_elapsed = time.time() - start_time
                print(searched_word + " is NOT IN the dictionary. (" + str(time_elapsed) + " seconds)")
                user_selection = input("Enter menu selection (1-5): ")
        
        elif user_selection == '3':
            not_found = 0
            start_time = time.time()
            print("Linear Search starting...")

            for i in range (len(aliceWords)):
                pos = linearSearch(dictionary, aliceWords[i].lower())
                if pos == -1:
                    not_found += 1
    
            time_elapsed = time.time() - start_time
            print("Number of words not found in the dictionary: " + str(not_found) + " (" + str(time_elapsed) + " seconds)")
            print("\n" + options)
            user_selection = input("Enter menu selection (1-5): ")

        else:
            not_found = 0
            start_time = time.time()
            print("Binary Search starting...")

            for i in range (len(aliceWords)):
                pos = binarySearch(dictionary, aliceWords[i].lower())
                if pos == -1:
                    not_found += 1
    
            time_elapsed = time.time() - start_time
            print("Number of words not found in the dictionary: " + str(not_found) + " (" + str(time_elapsed) + " seconds)")
            print("\n" + options)
            user_selection = input("Enter menu selection (1-5): ")

# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


def linearSearch(anArray, item):
    for i in range (len(anArray)):
        if anArray[i] == item:
            return i
    return -1
    


def binarySearch(anArray, item):
    li = 0
    ui = len(anArray) - 1
    while li <= ui :
        mi = (li + ui) // 2
  
        if(item == anArray[mi]):
            return mi
        elif(item < anArray[mi]):
            ui = mi - 1
        else:
            li = mi + 1 
    return -1

def search_again():
    options = "Main Menu \n 1: Spell Check a Word (Linear Search) \n 2: Spell Check a Word (Binary Search) \n 3: Spell Check Alice In Wonderland (Linear Search) \n 4: Spell Check Alice In Wonderland (Binary Search) \n 5: Exit"
    print("\n" + options)
    user_selection = input("Enter menu selection (1-5): ")

# Call main() to begin program
main()
