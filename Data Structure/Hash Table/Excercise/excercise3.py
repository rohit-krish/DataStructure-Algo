'''
    QUESTION 3.
    poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
    You have to read this file in python and print every word and its count as show below.
    ``
        'diverged': 2,
        'in': 3,
        'I': 8
    ``
    Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
'''

words_count_dict = {}

with open('./poem.txt', 'r')as f:
    for line in f:
        token = line.split(' ')
        for i in token:
            if i in words_count_dict:
                words_count_dict[i] += 1
            else:
                words_count_dict[i] = 1

print(words_count_dict)
