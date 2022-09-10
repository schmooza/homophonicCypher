import random
import string
from itertools import chain
import csv

globalVarIndex = 0
finalDict = {}


def generateAZList():
	aToZList = []
	for letter in string.ascii_lowercase:
		aToZList.append(letter)

	print (aToZList)
	return aToZList

def popLetterFromAZListMakeItKey(aToZList):
	keyIs = aToZList.pop(0)
	print (keyIs,"debug")
	return keyIs



def makeListsOfUniqueNums():
	possibleNumList = []
	aList = []

	for n in range (1,101):
		possibleNumList.append(n)

	print (possibleNumList)
	return possibleNumList



def chooseThreeNums():
	global numberList
	x = len(numberList)
	print("current number list is" , numberList)
	aListTemp = []
	for n in range(0,3):
		print(n)
		valueToAdd = random.choice(numberList)
		numberList.remove(valueToAdd)
		aListTemp.append(valueToAdd)

	print(aListTemp, f"should be random 3 numbers from a set of {x} unique numbers.")
	# delete the 3 selected numbers from the number list



	return aListTemp





def combineKeysAndValsIntoDict(keyIs, ValsAre):
	encodeList = dict.fromkeys(keyIs, ValsAre)
	print(encodeList)
	return encodeList

def listName():
	return

# def writeToCsv(outputToCsv):


# def checkErrors(csv):


def exportToCSV(dictionaryToExport):


	with open('cypher.csv', 'w') as f:
		for key in dictionaryToExport.keys():
			x = str(dictionaryToExport[key])


			f.write("%s, %s\n" % (key, x.lstrip("[").rstrip("]")))

# makes a list of x numbers
numberList = makeListsOfUniqueNums()
# makes a list of a-z letters
azList = generateAZList()

# cycles through the range of the list of letters.
while len(azList)>0:
	# gets a letter from the a-z list
	extractedLetterList = popLetterFromAZListMakeItKey(azList)
	# picks 3 unique numbers from the n number list
	currentListOfThreeUniqueNums = chooseThreeNums()
	# makes a dictionary using the letter as a key and the 3 numbers as the values.
	dictForEncoding = combineKeysAndValsIntoDict(extractedLetterList,currentListOfThreeUniqueNums)
	finalDict.update(dictForEncoding)



exportToCSV(finalDict)



print ("final dictionary to use for the cypher", finalDict)