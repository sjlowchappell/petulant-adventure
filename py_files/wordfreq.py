#Samuel Low-Chappell
#260565530

#The following algorithm works for stripping and counting
#the words. Now I just need to figure out the file I/O bit
import sys
import os

#error checking:
#ensures that arguments were entered properly
#and that the file exists
if len(sys.argv)!=2:
	print "Error: Improper number of arguments. Should be 2."
else:
	file_name=sys.argv[1]
	if not os.path.exists(file_name):
		print "Error: File not found"
	else:
		with open (file_name, "r") as textFile:
			full_text=textFile.read().replace('\n', '')

		textFile.close()

		words=full_text.split()							#splits the file into a list of words
		for idx, i in enumerate(words):					#for loop for going through each word
			words[idx]=i.lower().replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace(',', '').replace('.', '').replace(':', '').replace(';', '').replace('!', '').replace("'", "").replace('"', '')  #and removing punctuation
		words.sort()									#sort the words so it's easy to 
														#count them
		count=0
		comp_word=words[0]
										
		for idx, i in enumerate(words):					#for loop goes through the words list
			if(comp_word==i):							#counts however many of the same word
				count=count+1   						#appears in a row. Once there are
			else:										#no more words that appear in a row
				print comp_word, count   				#it prints the word and the number
				comp_word=i 							#of times it appears
				count=1  								#Then, moves onto the next word and 
		print comp_word, count 							#restarts the count
