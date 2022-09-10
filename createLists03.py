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
	# note, 1-9 are problematic as they should be 01, 02 etc
	possibleNumList = []
	aList = []

	zeroDigitList = ["01","02","03","04","05","06","07","08","09"]
	for n in zeroDigitList:
		possibleNumList.append(n)
	print(possibleNumList,"debug 22")
	# NOTE the cypher works with pairs of 2 digit numbers, atm. It could be any pairs of n digits. e.g. 333, 445, 777
	for n in range (10,100):
		possibleNumList.append(str(n))

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

		#_________________________ could be problematic.
		removeQuoteMarks = int(valueToAdd)
		aListTemp.append(removeQuoteMarks)

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


	with open('cypher2.csv', 'w') as f:
		# makes a header
		header = "key,val01,val02,val03"
		f.write(header)

		for key in dictionaryToExport.keys():
			x = str(dictionaryToExport[key])

			f.write("\n")
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