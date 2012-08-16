# find largest prime number of a composite number
# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143

# this is a more efficient solution


# 2 is the only even prime number
# if number is even, divide by 2 until you get an odd number
# and set the biggest factor so far to be 2
# otherwise, the biggest factor so far has to be 1
if number % 2 == 0:
	number = number / 2
	biggestFactor = 2
	while number % 2 == 0:
		number = number / 2
else:
	biggestFactor = 1

# the first factor to consider is 3, 2 greater than 1
# there's no point in considering evens (4, 6, 8, etc.)
prime = 3

# loop until the number is not greater than 1
while number > 1:
	# if prime is a factor of number
	# divide number by prime until number is not
	# the biggest factor so far is therefore the prime
	if number % prime == 0:
		number = number / prime
		biggestFactor = prime
		while number % prime == 0:
			number = number / factor
	prime = prime + 2

print(prime)

# this is my original implementation
# it's very inefficient with big numbers
# I wrote it just to brute-force the Euler problem
# then I went back and updated it to the above after some thinking
#currentPrime = 2
#primes = []

#while currentPrime <= number:
	# if the composite number is divisible by the current prime
	# add the prime to the list of prime factors of that number
	#if number % currentPrime == 0:
		#primes.append(currentPrime)

		# for the prime just added, loop through the list of current primes
		# if the current prime isn't prime, remove it
		#for i in primes:
			#if currentPrime % i == 0 and currentPrime != i and currentPrime in primes:
				#primes.remove(currentPrime)

	#currentPrime = currentPrime + 1

# print the largest prime factor of the given composite number
#print(primes.pop())