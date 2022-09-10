import pandas as pd
import random


def pickRandomValFromList(currentListOfVals):
	print(repr(currentListOfVals), "debug33")
	print(type(currentListOfVals))
	print(len(currentListOfVals))





# imput the data
df = pd.read_csv('cypher2.csv')
pd.options.display.max_rows = 9999
print(df)

# input string to encode
encodeListOfStrings = []
encodedData = []
encodeString = input("Sentence to encode:")
for n in encodeString:
	encodeListOfStrings.append(n)

print (encodeListOfStrings, "debug")
for n in encodeListOfStrings:
	tempList = []
	# checks the letter is in the data set, if true continue
	print(n in df['key'].unique())

	# checks the input and matches it to the csv data. input = "a" -> csv data has a in the key col. thus the index is determined
	indexValIs = df.index[df['key']==n]

	# the index value of the input data.

	z = indexValIs.tolist()
	#makes a new data frame.
	possibleNumValsOfTheInput = df.iloc[z]

	extractedListFromSelectedData = possibleNumValsOfTheInput.values.tolist()
	print (extractedListFromSelectedData,'debug11')

	print(type(extractedListFromSelectedData))

	# the mr. s way to get a list out of a list, needs fixing but works for now. picks a random element from
	# a choice of 1. like removing the shell of a nut.

	hackIt = random.choice(extractedListFromSelectedData)
	# slices the list removing the first element -> string (which corresponds to the input entered by the user).
	# I should convert the letters to numbers, which would be more gooder by not as easy to read.
	hackIt2 = hackIt[1:]
	print(hackIt2)
	theNumberPickedFromTheListOfPossibleNumbersCorrespondingToTheDataToEncode = random.choice(hackIt2)
	print(theNumberPickedFromTheListOfPossibleNumbersCorrespondingToTheDataToEncode)
	encodedData.append(theNumberPickedFromTheListOfPossibleNumbersCorrespondingToTheDataToEncode)


print(encodedData)








	


		# deletes index zero using slicing
		# justNumbers = tempList[1:]
		# print(justNumbers,"should be just numbers")
		# picks a number from the list




