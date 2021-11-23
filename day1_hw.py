import re
# exercise 1

words = ['this', 'is', 'a', 'sentence', '.']


def reverseList(list):
    list[0], list[1], list[2], list[3], list[4] = list[4], list[3], list[2], list[1], list[0]
    return list


print(reverseList(words))

# exercise 2
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


def getDict(string):
    dict = {}
    pattern = re.compile('[A-Za-z]+')
    new_list = pattern.findall(string)
    for word in new_list:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict


print(getDict(a_text))

# exercise 3

nums_list = [10, 23, 45, 70, 11, 15]
target = 70
# If number is not present return -1


def findTarget(list1, targ):
    for num in list1:
        if num == targ:
            return num
    else:
        return list1[-1]


print(findTarget(nums_list, target))
print(findTarget(nums_list, 22))
