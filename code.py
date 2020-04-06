# Given two arrays, determine if both arrays contain exactly the same elements, regardless of their order.

# Input: [Int], [Int]
# Output: Bool

# Test Case:

# [1,3,4,5,6,1]
# [1,6,5,4,3,1]
# True

#  Iterate through both arrays and store a count of each element
#  Compare if both histograms are equal

def two_arrays(arr1,arr2):

	hist1 = {}
	hist2 = {}

	for i in arr1:
		if i in hist1:
			hist1[i] += 1
		else:
			hist1[i] = 1

	for i in arr2:
		if i in hist2:
			hist2[i] += 1
		else:
			hist2[i] = 1

	return hist1 == hist2

# Time Complexity: 0(n)
# Space Complexity: 0(n)



# Given an array a of numbers and a target value t, find two numbers that sum to t

# Input: [Int], Int
# Output: [Int]
# Test Case: 

# [1,3,4,9,8] , 7
# [3,4]


# Create a hashtable 
# Iterate through array
	# Check if x is in hashatable
		# return x and current number
	# Add current number to hasbtable
# Return None

def two_sum(arr, target):
	dict = {}
	for i in arr:
		if target - i in dict:
			return (target - i, i)
		dict[i] = True
	return None

# Time Complexity: O(n)
# Space Complexity: 0(n)













