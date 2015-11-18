#Samuel Low-Chappell
#260565530


import difflib
import pickle
import sys
import os

#error checking:
#ensures that arguments were entered properly
#and that the file exists
if len(sys.argv)!=2:
	print "Error: Improper number of arguments. Should be 2."
else:
	pickle_name=sys.argv[1]
	if not os.path.exists(pickle_name):
		print "Error: File not found"
	else:
		pairs_dict=pickle.load(open(pickle_name, "r"))

		#infinite loop so you can keep spell checking
		while 1:
			key_words=""
			keys=[]
			fix=""
			suggestions_list=[]
			#get input from the user
			key_words=raw_input("Enter a pair of words: ")
			key_list=key_words.split()								
			
			#checks for valid input
			while len(key_list)!=2:
				print "Error: Invalid input, try again."						
				key_words=raw_input("Enter a pair of words: ")	
				key_list=key_words.split()										

			word_1=key_list[0]
			word_2=key_list[1]
			#puts the input in the same form as the 
			#elements of the dictionary
			key_words=str(key_list)

			#checks to see if the words are in the dictionary, if so, returns a positive response
			if key_words in pairs_dict:
				print "Well spelled!"
			#if they are not in the dictionary, it gives the closest fix
			else:
				#goes through the close matches of the user input
				#in the dictionary
				for i in difflib.get_close_matches(key_words, pairs_dict, 10):
					foo=i.split()
					#iterates through the close matches making comparisons to check frequency
					#of use.
					#sets the fix to be the pair with the highest frequency
					#Then, prints the first word in fix with the
					#second word of user input, as indicated in the a3 PDF
					count=pairs_dict.get(i)
					if (count>pairs_dict.get(fix)):
						fix=i
				final_form=fix.split()

				print "Fix: ", final_form[0].replace("['", "").replace("',", "").replace("'", "").replace("]", ""), word_2