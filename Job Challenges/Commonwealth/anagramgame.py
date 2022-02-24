import urllib.request
from collections import Counter

# Declaration of variables
letterset = "areallylongword"
scores = {}


# Checks if the word inputted by the user is in the wordlist
#
# @parameter user_wordinput <- Word inputted by the user

def checkword(user_wordinput): 
    data = urllib.request.urlopen("https://cwcodetest.s3.ca-central-1.amazonaws.com/wordlist.txt")
    for line in data:
        line_words = line.decode('utf-8').split()
        if line_words[0] == user_wordinput:
            return True

# Checks if any letters are used more than once hence duplicate of letters
#
# @parameter user_wordinput <- Word inputted by the user

def checkforduplicates(user_wordinput):
    duplicate = Counter(user_wordinput)
    for letter,number in duplicate.items():
        if number > 1:
            return False
    return True

# Checks if each letter in the word inputted by the user appears in the letterset
#
# @parameter user_wordinput <- Word inputted by the user

def checkforletterset(user_wordinput):
    counter = 0
    for letters in user_wordinput:
        for letter in letterset:
            if letters == letter:
                counter += 1
                break
    if counter == len(user_wordinput):
        return True
    else:
        return False


print("\nWelcome to the Anagram Game by Martin Tang")

while True:

    #Prompts the user for input
    print("\nThe Letter Set is: %s \n" %letterset)
    inputword = input("1. Enter /no to Quit \n2. Print /score to see the Top 10 Highest Submissions \n3. Enter /letterset to change the Letter Set \n4. Enter a word to play: ")
    
    # Command for users to quit
    if inputword == "/no":
        print("\nThank you for playing! Have a great day")
        break
    
    # Command for users to view the score
    elif inputword == "/score":
        print("\n    Top 10 Highest Scores \n")
        sortedscores = Counter(scores)
        for word,score in sortedscores.most_common(10):
            print("%15s - %s" % (word, score)) 
        print("\n")
    
    # Command for users to change the letterset
    elif inputword == "/letterset":
        changeset = input("\nEnter the word you want to become the letterset: ")
        letterset = changeset
    
    # Validation for user input
    else:
        if checkforduplicates(inputword):
            if checkforletterset(inputword):
                if checkword(inputword):
                    print("\n %s is VALID - Score Counted\n" % inputword)
                    scores[inputword] = len(inputword)
                else:
                    print("\n NOT VALID - Not found in databse \n")       
            else:
                print('\n NOT VALID - Not found in letter set \n')
        else:
            print('\n NOT VALID - Duplicates \n')