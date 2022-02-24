import urllib.request
from collections import Counter

letterset = "areallylongword"
scores = {
    "Score #1": 0,
    "Score #2": 0,
    "Score #3": 0,
    "Score #4": 0,
    "Score #5": 0,
    "Score #6": 0,
    "Score #7": 0,
    "Score #8": 0,
    "Score #9": 0,
    "Score #10": 0,
}


def checkword(user_wordinput):
    data = urllib.request.urlopen("https://cwcodetest.s3.ca-central-1.amazonaws.com/wordlist.txt")
    for line in data:
        line_words = line.decode('utf-8').split()
        if line_words[0] == user_wordinput:
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
    inputword = input("1. Enter /no to Quit \n2. Print /score to see the Top 10 Highest Submissions \n3. Enter a word to play: ")
    if inputword == "/no":
        print("\nThank you for playing! Have a great day")
        break
    elif inputword == "/score":
        print("\n  Top 10 Highest Scores \n")
        sortedscores = Counter(scores)
        for word,score in sortedscores.most_common(10):
            print("%15s - %s" % (word, score)) 
        print("\n")
    else:
        if checkforduplicates(inputword):
            if checkforletterset(inputword):
                if checkword(inputword):
                    print("\n")
                    print(inputword, "is Valid - Score Counted\n")
                    scores[inputword] = len(inputword)
                else:
                    print("Not found in databse")       
            else:
                print('Not found in letter set')
        else:
            print('Duplicates')