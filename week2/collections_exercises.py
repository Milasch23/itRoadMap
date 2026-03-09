# 1 - Element frequency
# Given a list of numbers, create a dictionary that counts how many times each element appears

def freq_count(list):
    frequencies = {}
    for i in list:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies

num_list = [1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 1, 4, 6, 6, 6, 7]
print(freq_count(num_list))


# 2 - Common elements
# Given two lists, obtain a set with the elements that appear in both.
def in_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    inters = set1.intersection(set2)

    return inters

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]

print(in_common(list_a, list_b))


# 3 - Lengths with list comprehension
# Given a list of words, create a new list containing the length of each word, using list comprehension.

def word_lenghts(words):
    return [len(word) for word in words]

some_words = ["Hello", "All", "Cheers"]
print(word_lenghts(some_words))

