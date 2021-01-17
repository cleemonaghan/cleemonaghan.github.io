# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:05:10 2021

@author: Colin
"""

"""
Problem 2.4
This function takes a number max as an input,and outputs all prime numbers from 1 to max.
For instance, primes(10) should return the list [2,3,5,7].
"""
def primes(max):
    if(max < 2):
        return []
    prime = []
    for value in range(2,max+1):
        boolean = True
        for factor in prime:
            if(value % factor == 0):
                # If we found a factor, it is not a prime
                boolean = False
                break
        if(boolean): 
            prime.append(value)
    return prime


"""
Problem 2.5
This function takes a number as an input and returns its prime factorization: a list of prime numbers whose product is n.  
For instance, prime_factorization(120) should return [2,2,2,3,5]
"""
def prime_factorization(number):
    solution = []
    #If zero, return an empty list
    if(number == 0):
        return solution
    #If negative, add -1 to the list and negate the inputed number
    elif(number < 0):
        number = -number
        solution.append(-1)
    #Get the list of primes less than the inputed number
    primesList = primes(number)
    while number > 1:
        for value in primesList:
            if(number % value == 0):
                # We found a factor
                number = number/value
                solution.append(value)
                break
    return solution

"""
Problem 2.6
This function takes a list and returns a sorted version using the heapsort algorithm.
For instance, my_sort([3,1,2]) returns the list [1,2,3].  
"""
def my_sort(array):
	#stage 1: create the heap
	arrayLength = len(array)

	#start at the back of the array and compare each child to it's parent
	#each parent must be bigger than it's children
	for child in range(arrayLength-1, 0, -1):
	#compare child to it's parent, if child is bigger sink the parent
		if array[child] > array[(child-1)//2]:
			#sink the parent
			sink(array, (child-1)//2, arrayLength)
	

	#now array is a heap

	#stage 2: move the largest element to the back and reform the heap
	#the size of the unsorted array
	unsortedSize = arrayLength-1

	#while the unsorted array still can be sorted
	while unsortedSize >= 0:
		#move the largest to the back
		element = array[0]
		array[0] = array[unsortedSize]
		array[unsortedSize] = element
		#sink the unsorted element at index 0 into the proper place
		sink(array, 0, unsortedSize)
		#decrease size of unsorted array by 1
		unsortedSize -= 1
	return array

def sink(array, parent, size):
	while parent < size:
		#if the parent has a left child
		if (2*parent)+1 < size:
			#the bigger child becomes the left child
			bigChild = (2*parent)+1
			if (2*parent)+2 < size and array[bigChild] < array[(2*parent)+2]: 
				bigChild = (2*parent)+2
			#if the parent is smaller than its child, swap them
			if array[parent] < array[bigChild]:
				element = array[parent]
				array[parent] = array[bigChild]
				array[bigChild] = element
				#follow the parent element, it is now at the bigChild's index
				parent = bigChild
			
			#if it is larger than its children, end the sink
			else: return True
		#if there are no more children, end the sink
		else: return True
	

"""
Problem 2.7
The encrypt function encrypts a text file using some secret code, and 
the decrypt function decrypts it, making it readable again.  
"""
def encrypt(filename):
	file = open(filename, "r")
	output = open("encoded_"+filename, "w")
	
	#the exponent and prime values
	exponent = 3
	prime = 131
	
	
	#Loop through the lines of the file
	lines = file.readlines()
	for line in lines:
		#encode each letter of the line and add it to the output file
		encoded_line = ''
		for letter in line:
			number = ord(letter)
			encoded_line += '{},'.format((number**exponent) % prime)
		output.write(encoded_line)
	file.close()
	output.close()

def decrypt(encypted_filename):
	file = open(encypted_filename, "r")
	output = open("decypted_"+encypted_filename, "w")
	#the exponent and prime values
	inverse = 87    #exponent*inverse is conguent to 1 modulo prime-1
	prime = 131
	

	#Loop through the lines of the file
	lines = file.readlines()
	for line in lines:
		#split the line up by commas
		numbers = line.strip().split(',')
		#decode each number of the line and add it to the output file
		decoded_line = ''
		for number in numbers[:-1]:
			letter = chr(((int(number)**inverse) % prime))
			decoded_line+=letter
		output.write(decoded_line)
	file.close()
	output.close()

"""
Problem 2.13
This function takes in a number of cents (US currency) and returns all the 
different ways to make that number of cents using US coins, of values 1 cent, 
5 cents, 10 cents, and 25 cents. The result is a list of reverse-sorted lists. 

So for instance, make_change(11) should return 
[[1,1,1,1,1,1,1,1,1,1,1],[5,1,1,1,1,1,1],[5,5,1],[10,1]].  
These represent 11 pennies, 1 nickel 6 pennies, 2 nickels 1 penny, and 
1 dime 1 penny, which are all four ways to make 11 cents.
"""
def make_change(cents):
	solutions = []
	ones = []
	#find the solution of all ones
	for index in range(cents):
		ones.append(1)
	#add this solution to the list of solutions
	solutions.append(ones)
	
	#derive the other solutions from the original solution
	solution = ones[:]
	#check if we can exchange 5 ones for 1 five
	while solution.count(1) >= 5:
		solution = solution[5:]
		solution.append(5)
		solution.reverse()
		solutions.append(solution[:])
		solution.reverse()
		solution1 = solution[:]
		#check if we can exchange 2 fives for 1 ten
		while solution1.count(5) >= 2:
			solution1.remove(5)
			solution1.remove(5)
			solution1.append(10)
			solution1.reverse()
			solutions.append(solution1[:])
			solution1.reverse()
			solution2 = solution1[:]
			#check if we can exchange 1 five and 2 tens for 1 twenty-five
			while solution2.count(5) >= 1 and solution2.count(10) >= 2:
				solution2.remove(10)
				solution2.remove(10)
				solution2.remove(5)
				solution2.append(25)
				solution2.reverse()
				solutions.append(solution2[:])
				solution2.reverse()
			
		
	
	#return the list of solutions
	return solutions

"""
Problem 2.8
This function takes a string of letters and returns a list of English 
words from the list which consist of exactly the letters from the string.
For instance, unscramble("eilnst") could return 
["enlist","listen","silent","inlets","tinsel"].
"""
def unscramble(word):
	output = []
	
	file = open('wordlist.txt', "r")
	
	#Loop through the lines of the file
	lines = file.readlines()
	for line in lines:
		line = line.strip()
		#determine if they contain the same letters
		if len(line) != len(word):
			continue
		match = True
		for letter in word:
			if word.count(letter) != line.count(letter):
				match = False
				break
		if match:
			output.append(line)
	file.close()
	return output




