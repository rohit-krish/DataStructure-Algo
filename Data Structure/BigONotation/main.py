'''
Big O Notation is used to measure how running time or space requirements for your program grows as the input grows
'''


def getSquaredNumbers(numbers):
    return [n*n for n in numbers]
    # time complexity is O(n)


def find_first_pe(prices, eps, index):
    return prices[index]/eps[index]
    # time complexity is O(1)


def findDuplicate(numbers=[1, 2, 3, 4, 5, 1, 3, 4]):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                print(numbers[i], 'is a duplicate')
    # time complexity is O(n^2)
