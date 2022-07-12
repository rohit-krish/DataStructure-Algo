'''
There are static array and dynamic array
In python list is implemented as dynamic array
In other languages like JAVA,C++ we have static aswell as dynamic array

In static array size is static,
In dynamic array size is dynamic(initially it allocate some space on memory,
    then as we keep inserting new data to it,the allocated space will be full,
    even after we try to insert a data the program finds another block of memory which have double the size then it initially had)
'''
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

heros.insert(3, 'black panther')
print(heros)

oddNumbers = [odd for odd in range(10) if odd % 2 != 0]
print(oddNumbers)
