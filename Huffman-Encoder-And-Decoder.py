# ASB #
import numpy as np
		
																		#* Stage 1 : Get text which need to be encoded. remove spaces,lowercase all chars,remove numbers.

text = input("\nEnter Text :")

#Lowercase , delete spaces, remove numbers
#text = text.replace(" ", "")     													# remove spaces
text = text.lower()             													# lower all cases
for i in range(10):              													# remove numbers
	text = text.replace(str(i),'')
#print("(TEST)text=",text) 															# TEST

																		#* Stage 2 : Count repetition of every unique member in text string. Store chars and repetition numbers in lists.

																				# Order numbers for a character in charList is identical in charCount list which represents a repetition number for that character
																				# example:
																				# charList =  ['a','b','c','d', ...]
																				# charCount = [ 3 , 6 , 1 , 4 , ...]

charList = list()																	# list that hold all unique characters in text string
for i in range (len(text)):
	if text[i] not in charList:													# duplicate members are not allowed!
		charList.append(text[i])			
#print("(TEST)charList=",charList) 												# TEST


charCount = list()																	# list for count number of all unique characters (which stored in char_set)
for i in range (len(charList)):
	charToCount = charList[i]
	count_number = text.count(charToCount)
	charCount.insert(i,count_number)												# charCount is a list that holds repetition times in test string, for all character that charList holds.
#print("(TEST)charCount=",charCount) 												# TEST

																			#* Stage 3 : Order charCount list from biggest to smallest and keep the alignment between charList
												

for j in range (len(charList)-1):													# sort values of charCount list from biggest to smallest using bubble sorting algorithm
	for i in range (len(charList)-1):				
		if charCount[i+1] > charCount[i]:
			temp = charCount[i]
			charCount[i] = charCount[i+1]
			charCount[i+1] = temp
			temp = charList[i]														# apply the same sorting changes for charList to keep the alignment with charCount list
			charList[i] = charList[i+1]
			charList[i+1] = temp
#print("(TEST)charList sorted=",charList)											#TEST
#print("(TEST)charCount sorted=",charCount)										#TEST

																			#* Stage 4: Create two-dimensional matrix for decision matrix building.
																			# characters that share the same leaf are stored in same column. 
																			# charCount list keeps the alignment and hold the total value of all characters sharing same column
												
charList2 =  [[0 for x in range(len(charList))] for y in range(len(charList))]  	# two-dimensional matrix for stacking characters for decision matrix building
for i in range (len(charList)):													# characters that stacked share the same column in matrix. their values are summed
	charList2[0][i] = charList[i]
#print("(TEST)charList2=\n",np.matrix(charList2))									#TEST									


#BUİLD DECİSİON MATRİX

encodedChar = list()	    														# 2 matrix for storing each characters huffman coded representation with bits
encodedValue = [[] for i in range(len(charList))]

encodedChar = charList.copy()													 	# first row hold each character used in text
																					# second row will hold each characters encoding path
#print("(TEST)encodedChar matrix=",encodedChar)									#TEST
#print("(TEST)encodedValue matrix=",encodedValue)									#TEST

#print("(TEST)Beginning to setup Decision Matrix:")									#TEST

for i in range (len(charList)-1):
	#print("(TEST)Column=",-i)														#TEST
	for rightRow in range (len(charList)):
		if charList2[rightRow][-(i+1)] != 0:
			for j in range(len(charList)):
				if encodedChar[j] == charList2[rightRow][-(i+1)]:
					encodedValue[j] += '0'
					#print("(TEST)(i=%d)encodedChar=" %i,encodedChar)				#TEST
					#print("(TEST)(i=%d)encodedValue=" %i,encodedValue)			#TEST
					break
	for leftRow in range (len(charList)):
		if charList2[leftRow][-(i+2)] != 0:
			for j in range(len(charList)):
				if encodedChar[j] == charList2[leftRow][-(i+2)]:
					encodedValue[j] += '1'
					#print("(TEST)(i=%d)encodedChar=" %i,encodedChar)				#TEST
					#print("(TEST)(i=%d)encodedValue=" %i,encodedValue)			#TEST
					break

	for row in range (len(charList)):
		if charList2[row][-(i+2)] == 0:
			for row2 in range (len(charList)):
				if charList2[row2][-(i+1)] != 0:
					charList2[row][-(i+2)] = charList2[row2][-(i+1)]
					charList2[row2][-(i+1)] = 0
					
					
					#print("(TEST)(i=%d) ,row1=%d ,row2=%d" %(i,row,row2) )			#TEST
					#print("(TEST)(i=%d)charList2=\n" %i,np.matrix(charList2))		#TEST
					break
		charCount[-(i+2)] += charCount[-(i+1)]
		charCount[-(i+1)] = 0
	
	
	for b1 in range (len(charCount)-1):											#Bubble Sorting for charList2 and charCount at every i step
		for b2 in range (len(charCount)-1):
			if charCount[b2] < charCount[b2+1]:
				temp = charCount[b2]
				charCount[b2] = charCount[b2+1]
				charCount[b2+1] = temp
				
				for x in range (len(charList)):
					temp = charList2[x][b2]
					charList2[x][b2] = charList2[x][b2+1]
					charList2[x][b2+1] = temp
		
			
	
	#print("(TEST)(i=%d)charCount=\n" %i,np.matrix(charCount))						#TEST
	
#print("(TEST)(Final)charList2=\n",np.matrix(charList2))
#print("(TEST)(Final)charCount=\n",np.matrix(charCount))
#print("(TEST)(Final)encodedChar=",encodedChar)
#print("(TEST)(Final)encodedValue",encodedValue)

for i in range (len(encodedValue)):												#reverse bits order for each character
	encodedValue[i].reverse()
	
#print("(TEST)(Final)encodedValue(after reverse)",encodedValue)


encodedText = ""																	#empty string for encoded text display

if len(encodedChar)>1:
	for t in range (len(text)):
		for c in range (len(encodedChar)):
			if text[t] == encodedChar[c]:
				for v in range(len(encodedValue[c])):
					encodedText += encodedValue[c][v]
				break
else:
	
	encodedValue[0] = '0'
	for i in range(len(text)):
		encodedText += '0'

																		#* Stage 5: Show results
print("\n########## Results ##########")																		
print("\nInput Text=",text)
print("\nCharacter=",encodedChar)
print("Value=    ",encodedValue)			
print("\nEncoded Text(bitwise)=",encodedText)


																		#* Stage 6: Decoding encoded text
																		
decodedText = "" 
parsedText = ""
currentCharValue = ""
for t in range (len(encodedText)):
	parsedText += encodedText[t] 
	
	for i in range (len(encodedChar)):
		for b in range (len(encodedValue[i])):
			currentCharValue += encodedValue[i][b]
		if parsedText == currentCharValue:
			decodedText += encodedChar[i]
			parsedText = ""
			break
		currentCharValue = ""

print("\nDecoded Text=",decodedText)




	


