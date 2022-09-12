import pandas as pd
import numpy as np

pd.options.display.max_rows = 9999

dfEncodedData = pd.read_csv('encodedDataMessage.csv')

dfCypherKey = pd.read_csv('cypher2.csv')
# print(dfEncodedData)
# print(dfCypherKey)

resultList = []

# print(dfEncodedData["message"])


for n in dfEncodedData["message"]:
	print (type(n))
	# finds the index that matches the string data. makes a new column called new.
	dfCypherKey["new"]= dfCypherKey.apply(lambda row: row.astype(str).str.contains(n).any(), axis=1)

	#checks if "new" has a True value
	for n in dfCypherKey["new"]:
		if n == True:

			# if the row has True in it, extract this row.
			rowIs = dfCypherKey.loc[dfCypherKey['new'] == True]
			print(rowIs,"the goods")

			x = rowIs["key"]
			print(x)
			y = x.to_string()


			resultList.append(y)




cleanedResults = []

print(resultList)
for n in resultList:
	length = len(n)
	print (length)
	print(type(n))
	lastChar = n[-1:]
	cleanedResults.append(lastChar)

print(cleanedResults)
magicWord ="".join(cleanedResults)

with open('finalResults.txt', 'w') as f:
	f.write(magicWord)






#



# with open("finalResults.txt", "w") as f:
# 	f.write(stringResults)

# gets the
# extractRawMessage = dfEncodedData.message
# print(extractRawMessage,"debug91")
# iterate through the data.

	# x = dfCypherKey["key"].str.find(n)
	# print(dfCypherKey['key'].where(dfCypherKey['val01' or 'val02' or 'val03'] == f"{n}"))



	# print(n, "debug31")
	# compares the two data sets, checks if the value is in the data.
	# if n in dfCypherKey.values:
	# 	print("data matches", n)


		# returns the key based on the possible number.

	# rows = dfCypherKey.loc[currentValueToDecode]
		# print (rows, "debug 37")
	# else:
	# 	print("false")




