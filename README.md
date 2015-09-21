# jumbler

## A note on submission
We will be working with and submitting our code to the codeguild2015/jumbler
github repo. Make sure that when you work on the repo, you make a unique
branch. After you and your partner are done working on your code, merge your
branch to the main branch. If there are no merge commits (there shouldn't be
if you named your program correctly) then push to the remote repo. Your file
should be in the main repo for me to clone. Also, make sure that you are
commiting regularly (after each atomic edit to your code) and using descriptive
commit messages.

## Purpose
A common programming task is to scan a file, picking out elements that meet some criterion. This assignment introduces the file-scan idiom in Python, along with some basic manipulation of strings (text).

## Pair Assignment
For this assignment we will be pair programming. Work together with one classmate.
Before writing code at the computer, you should work together and independently on the design. Each of you should be able to clearly explain how the program or a part of the program will work. When you are convinced that you both understand how the code will work, then and only then are you ready to write the code. After you have written code, submit your file as jumble_name1_name2.py to the main repo. Also clearly indicate the authors in the scripts header.

## Word Jumbles (Anagrams)
Anagrams are words whose letters have been scrambled. In newspapers and online, “word jumble” puzzles are based on anagrams, and can be solved using the program you will write. (For example, you should be able to solve the anagrams at the daily jumble.)

## Requirements
Your program will read two strings from the command line. The first is a scrambled word (e.g., “hinttree”). The second is the name of a file containing a list of words, which will serve as a dictionary. It will check the scrambled word against every word in the word list. If the scrambled word can be rearranged to match the dictonary word, the dictionary word will be printed. After scanning the whole word list, the program prints the number of matches and the number of words in the list. For example:

```
$ python3 jumbler.py trsesi dict.txt
resist
sister
2 matches in 41238 words
$ python3 jumbler.py rayin dict.txt
rainy
1 matches in 41238 lines
$ python3 jumbler.py tororo dict.txt
No matches
$ python3 jumbler.py taroro dict.txt
orator
1 matches in 41238 lines
$ 
```
Note that 41238 is the number of words found in that particular dictionary. We could also run the program with a shorter or longer dictionary (by typing a different file name in place of dict.txt), and would get a different word count.
```
$ python3 jumbler.py phaal shortdict.txt
alpha
1 matches in 5 lines
```
## Notes and hints on the jumble solver
Please name your program file jumbler_[names].py. This will prevent merge collisions in our repo.
I've provided some starter code in jumbler.py. Note there are three parts you need to make changes to, all marked with the text FIXME.

## How to check
There is a simple trick for matching anagrams in a word list: We sort the letters in the anagram (e.g., “trsesi” becomes “eirsst”), and we also sort the letters in each dictionary word before checking. Then, we can simply check to see if they match exactly.
Note: When python reads a line of text from a file, the line includes the ending carriage return and/or newline character. That's why we strip "white space" off the ends of each entry in the word list this way:
```
  word = word.strip()  # Remove spaces or carriage return at ends
```  
Python has a built-in function called sorted which puts any sequence into sorted order. A string (text) in Python is a kind of sequence, so you can use the sorted function to get the letters in a word in alphabetical order. The sorted function always returns a list, so for example sorted("resist") will return ["e", "i", "r", "s", "s", "t"]. Since we can check equality between lists, this can be fine. For example, if we check sorted("acb")==sorted("bca"), we will be comparing ["a", "b", "c"] to ["a", "b", "c"], and the result will be True.
You'll need a good word list to test your program. dict.txt will work.

You can find lots of test cases by searching for jumble or word jumble on the web.

## Grading
* 35 points possible
* 15: Program runs and consistently produces correct output for any scrambled word and any list of words. 

* 5 point penalty for any of the following:
  * Test cases running in addition to program functionality. (You need to 'comment out' the call to run_tests for your final testing and turn-in.)
  * Incorrect or missing counts of matches or items in the word list.
  * Other extra output, missing output, or output formatted differently than the examples above.
* 10: Follows PEP8 coding guidelines, including author identification and header.
* 10: Clarity. The program should not only be consistent with the requirements and approach described here, but it should be very easy to read the program and verify its consistency with the spec.
