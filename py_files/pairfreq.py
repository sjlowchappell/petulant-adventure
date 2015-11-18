#Samuel Low-Chappell


import pickle
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
		pickle_name=file_name[:-3]+"pickle"

		pairs=[]
		pairs_dict={}

		words=full_text.split()							#splits the file into a list of words
		for idx, i in enumerate(words):					#for loop for going through each word
			words[idx]=i.lower().replace('-', '').replace('?', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace(',', '').replace('.', '').replace(':', '').replace(';', '').replace('!', '').replace("'", "").replace('"', '')  #and removing punctuation
		for idx, i in enumerate(words[:-1]):			#for loop for making a list of word pairs
			pairs.append([i, words[idx+1]])
		pairs.sort()									#sort the pairs for easier counting

		count=0
		comp_pair=pairs[0]
										
		for idx, i in enumerate(pairs):					#for loop goes through the pairs list
			if(comp_pair==i):							#counts however many of the same pair
				count=count+1   						#appears in a row. Once there are
			else:										#no more pairs that appear in a row
				print comp_pair, count 					#it prints the pair and the number
				word_1=comp_pair[0]						#of times it appears. Then, moves onto
				word_2=(comp_pair[1])					#the next pair and restarts the count
				pairs_dict[str([word_1, word_2])]=count
				comp_pair=i 							
				count=1  							
		print comp_pair, count 							
														#It also adds the pair and the count
														#to the dictionary with the index being
														#the pair of strings and the count being
														#the value
		#dump the dictionary in a pickle
		pickle.dump(pairs_dict, open(pickle_name, "w"))
