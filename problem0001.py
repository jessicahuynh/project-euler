# of the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9
# the sum of these numbers is 23
# find sum of all multiples of 3 or 5 below 1000

sum = 0

for i in range(0,1000):
	if i % 3 == 0 or i % 5 == 0:
		sum += i
			
print(sum)