# Define a function that doubles even numbers and leaves odd numbers as it is
def even(num):
    if num%2==0:
        return num*2
    else:
        return num
numbers=[1,2,3,4,5,6,7]
lst=list(map(even,numbers))
print(lst)
