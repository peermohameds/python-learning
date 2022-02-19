from array import *

scores = array('I', [])
for i in range(1, 11):
    scores.insert(i, i + 10)
print("Length of array :", len(scores))
print("Data: ", scores)

# insert value in between
scores.insert(1,22)         # inserts 22 in position 1
scores.insert(-2,17)        # inserts 17 in position -2
print("Data: ", scores)

# accessing elements
print(scores[1])
print(scores[-3])
print(scores[-3:-1])        # accessing range

# removing elements: remove() can remove one by one
scores.remove(22)            # removing the first occurence of the value 22
print(scores)
# removing elements: pop() can remove  by index or rangeofindex
scores.pop(1) # removing element in index 1
print(scores)

# slicing an array
sliced_array = scores[3:7]
print("slice from 3 to 7",sliced_array)

sliced_array = scores[3:]
print("slice from 5 until end", sliced_array)

sliced_array = scores[:]
print("slice from 0 until end", sliced_array)

# changing value of array
sliced_array[3] = 100
print("assigned 100 to index 3", sliced_array)

# search the index of a first occurrence of value
print("index of value 100", sliced_array.index(100))
sum_array = sum(scores + sliced_array)
print("sum of arrays: ", sum_array)

print(sliced_array.itemsize)