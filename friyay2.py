
# Given two arrays write a function to find out if two arrays have the same frequency of digits.

def num_histogram(sentence): #takes a string, and returns a dictionary with letters for keys and tallies for values
    histogram = {}
    for num in sentence:
        if num in histogram:
            histogram[num] += 1
        else:
            histogram.update({num: 1})
    return histogram



def freq_check(dict1, dict2):
    dict3 = {}
    for key, value in dict2.items():
        dict3[key] = value
    for key in dict1:
        if key not in dict3:
            return False
        elif dict1[key] != dict3[key]:
            return False
        else:
            dict3.pop(key)
    if dict3 != {}:
        return False
    return True
# var1 = num_histogram([1, 2, 3, 4])
# var2 = num_histogram([1, 2, 3, 4, 2])
# print(var1)
# print(var2)
# print(freq_check(var1, var2))
# print(var1)
# print(var2)

#/////////////////////////////////
# Given two arrays write a function to determine if each value in our first array contains a corrsponding value
# to the second power in the second array.


def power_check(dict1, dict2):
    for key in dict1:
        if (key**2) not in dict2:
            return False
    return True 
# var1 = letter_histogram([1, 2, 3, 4])
# var2 = letter_histogram([1, 4, 9, 16])
# # print(var1)
# print(var2)
# print(power_check(var1, var2))

#///////////////////////////////////

def letter_histogram(sentence): #takes a string, and returns a dictionary with letters for keys and tallies for values
    histogram = {}
    for letter in sentence.lower():
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram.update({letter : 1})
    del histogram[" "]
    return histogram



def ana_check(dict1, dict2):
    dict3 = {}
    for key, value in dict2.items():
        dict3[key] = value
    for key in dict1:
        if key not in dict3:
            return False
        elif dict1[key] != dict3[key]:
            return False
        else:
            dict3.pop(key)
    if dict3 != {}:
        return False
    return True
str1 = letter_histogram("pie gi os od")
str2 = letter_histogram("pie is good")
# print(str1)
# print(str2)
# print(ana_check(str1, str2))
# print(str1)
# print(str2)

#/////////////////////////////////////

#Given a string return the letter that is used the most in the string.
#Use a dictionary to complete this solution.

def rank_top1(dict1):
    top = (' ', 0)
    for key,value in dict1.items():
        if value > top[1]:
            top = (key,value)
    return top[0]
print(rank_top1(letter_histogram("Blap Kablam bb")))