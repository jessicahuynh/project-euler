# for the terms in the Fibonacci less than 4 million, sum the even terms
limit = 4000000
firstTerm = 1
secondTerm = 1
evenNumber = firstTerm + secondTerm;
sum = 0

while (evenNumber < limit):
	sum += evenNumber
	
	# the third number in the sequence is always even
	firstTerm = secondTerm + evenNumber
	secondTerm = evenNumber + firstTerm
	evenNumber = firstTerm + secondTerm
	
print(sum)