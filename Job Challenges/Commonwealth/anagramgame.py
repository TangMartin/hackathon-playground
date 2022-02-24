import urllib.request
from collections import Counter

letterset = "areallylongword"
chars=[]


def checkword(user_wordinput):
    data = urllib.request.urlopen("https://cwcodetest.s3.ca-central-1.amazonaws.com/wordlist.txt")

    for line in data:
        line_words = line.decode('utf-8').split()
        if line_words[0] == user_wordinput:
            print('it works')
            return True


print("Welcome to the Anagram game")
print("The Word for Today is: areallylongword ")

inputword = input("Please enter a word: ")
print(inputword)

duplicate = Counter(inputword)

for letter,number in duplicate.items():
   if number > 1:
       print('fail')
       break; 





