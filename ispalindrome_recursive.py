def isPalindrome(strng):
	if len(strng) == 0:
		return True
	if strng[0] != strng[len(strng) - 1]:
		return False
	return isPalindrome(strng[1:-1])

#isPalindrome('ilikebacon')


def isOdd(num):
  if num % 2 == 0:
    return False
  else:
    return True

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if cb(arr[0]):
        return True
    return someRecursive(arr[1:], cb)

#print(someRecursive([1,2,3], isOdd))


def flatten(arr):
    result = []
    for a in arr:
        if type(a) == list:
            result.extend(flatten(a))
        else:
            result.append(a)
    return result

print(flatten([1,2,3, [4, 5, [1, 2, 3, 4, 5]]]))


def capitalize_first(arr):
    output_array = []
    for a in arr:
      new_str = a[0].upper() + a[1:]
      output_array.append(new_str)
    return output_array

print(capitalize_first(['car', 'taco', 'banana']))


def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    # Get the first character in the first array element, capitalize it, and append it to the first element, sliced to everything after that first index, so the 'c' in car becomes arr[0][0].upper() which becomes C
    # Then, we add it with arr[0][1:] which is 'ar' and upon appending these together we get Car, then we add it to the result array. 
    result.append(arr[0][0].upper() + arr[0][1:]) 
    # Then we add the current result array for this recursive call, plus the result of the calls after it. 
    # Because we are doing arr[1:] it will always be slicing the front of the array off by 1 each time we call this recursively. 
    # So the first call would be the arr[0] but then because the array is sliced, it would only be 2 elements in the second call, and so on and so on, each time we recurse, the front of the array (arr[0]) is removed. 
    return result + capitalizeFirst(arr[1:]) 

print(capitalizeFirst(['car', 'taco', 'banana']))
