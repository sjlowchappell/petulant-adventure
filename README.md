# petulant-adventure
A rudimentary spell checker created for my comp 206 course

This was one of my recent assignments. We had to create three files--a word counter, a word pair counter, and a spell-checker. 

**Word Counter**
The word counter takes a file as a command line argument, strips some punctuation, then prints each word of the file along with the number of times it appears in the file.

**Pair Counter**
The pair counter is very similar to the word counter. Rather than printing each word, it saves each pair of words as a key in a dictionary with the number of times the pair appears mapped as the value. It then dumps this information into a pickle file and prints the pairs with their counts to stdout.

**Spell Checker**
The spell checker is very rudimentary. It takes the pickle file created from the paircounter method as a command line argument and uses this dictionary to compare pairs of words entered by the user. The user must enter two words. The spell checker assumes the second word is spelled correctly. If the first word is spelled correctly, a positive response is printed to stdout. If the first word is spelled incorrectly, the program checks the dictionary for 10 close matches from the imported pickle dictionary and then prints the best fix to stdout.

