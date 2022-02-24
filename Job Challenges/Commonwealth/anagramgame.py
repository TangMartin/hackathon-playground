import urllib.request
from collections import Counter

letterset = "areallylongword"
dict = {
    "Score #1": "0",
    "Score #2": "0",
    "Score #3": "0",
    "Score #4": "0",
    "Score #5": "0",
    "Score #6": "0",
    "Score #7": "0",
    "Score #8": "0",
    "Score #9": "0",
    "Score #10": "0",
}


def checkword(user_wordinput):
    data = urllib.request.urlopen("https://cwcodetest.s3.ca-central-1.amazonaws.com/wordlist.txt")
    for line in data:
        line_words = line.decode('utf-8').split()
        if line_words[0] == user_wordinput:
            print('it works')
            return True

def checkforduplicates(user_wordinput):
    duplicate = Counter(user_wordinput)
    for letter,number in duplicate.items():
        if number > 1:
            return False
    return True

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


print("\nWelcome to the Anagram Game by Martin Tang\n")
print("The Word for Today is: areallylongword \n")

while True:
    inputword = input("1. Enter NO to Quit \n2. Print SCORE to see the Top 10 Highest Submissions \n3. Enter a word to play: ")
    if inputword == "NO":
        print("Thank you for playing! Have a great day")
    if checkforduplicates(inputword):
        if checkforletterset(inputword):
            if checkword(inputword):
                print("Word is found - Score Counted")
                print(len(inputword))
            else:
                print("Not found in databse")       
        else:
            print('Not found in letter set')
    else:
        print('Duplicates')
    





