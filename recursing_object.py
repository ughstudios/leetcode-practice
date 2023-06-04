obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}


def is_even(num):
    return num % 2 == 0


def nestedEvenSum(obj, sum=0):
    # the subproblem here is if it's an even number, add it to the sum, if it's another object, recurse through that object for even numbers
    for value in obj.values():
        if type(value) == dict:
            sum += nestedEvenSum(value)
        elif type(value) == int:
            if is_even(value):
                sum += value
        else:
            continue
    return sum
            
#print(nestedEvenSum(obj1))

words = ['i', 'am', 'learning', 'recursion']

def capitalize_words(arr):
  if len(arr) == 0:
    return arr
  # Capitalize this
  up = arr[0].upper()
  # do others
  words = capitalize_words(arr[1:])
  # prepend capitalized word to front of the list
  words.insert(0, up) # O(N - 1) to shift everything over? Depends on how .insert() is implemented
  # return all words
  return words

def capitalize_words2(arr):
  if len(arr) == 0:
    return arr
  resultArr = []
  resultArr.append(arr[0].upper())
  return resultArr + capitalize_words2(arr[1:])
   


#print(capitalize_words(words))

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

def stringifyNumbers(obj):
  for key, val in obj.items():
    if type(val) == dict:
      stringifyNumbers(val)
    if type(val) == int:
      obj[key] = str(val)
  return obj

#print(obj)
#print(stringifyNumbers(obj))


obj_strs = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}


def collect_strings(obj):
  resultStrings = []
  for key in obj.keys():
    if type(obj[key]) == dict:
      resultStrings.extend(collect_strings(obj[key]))
    if type(obj[key]) == str:
      resultStrings.append(obj[key])
  return resultStrings


print(collect_strings(obj_strs))

# With leetcode/hackerrank problems, the first step I feel would be to figure out what type of algorithm we are working with:
# Recursive? Iterative? BFS? DFS?