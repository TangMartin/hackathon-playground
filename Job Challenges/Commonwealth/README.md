<!-- TABLE OF CONTENTS -->
<h1 style="display: inline-block">Anagram Game</h1>

## About the Project: 
An anagagram game that ask users to create anagram words from a randomly shuffled wordlist. This game is only available in the console for now and can be played by following the steps below.

## How to Run:

1. Clone MAIN branch on your machine
2. Using the terminal navigate to sandbox/Job\ Challenges/commonwealth
3. type 'python3 anagramgame.py' and hit enter

## Functionalities

1. Wordlist is imported from https://cwcodetest.s3.ca-central-1.amazonaws.com/wordlist.txt
2. Users can change the letterset to their liking
3. Users can view their top ten scores in chronological order 

## What's Next

For this project, I wanted to step out of my comfort zone and program in a language which I am currently still learning. Because there isn't an interface at the moment, I wanted to use Python since it would be simpler to integrate it as a function to an endpoint that could later be connected to a web application with React. 

Furthur improvements include:

1. Flexibility in the wordlist that is used for validation (allow users to input their own wordlist via file or a url) - This allow users to have more freedom in the words they want to be tested and integrate non-english wordlists.
2. Incorporating defensive programming in the user's input by checking for edge cases as well as the prefiltered input such as spaces, symbols, or special characters
3. Experimenting with different algorithms rather than a linear search to optimize wordlist validation (ex. hashtable) - Due to how many words there are in the wordlist, this will increase the speed in finding whether the anagram word is in the list or not.



