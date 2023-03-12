# Program to take input from the user using strip and map method

n=int(input("Enter the size for the list"))
lst=list(map(int,input("Enter the list elements").strip().split()))[:n]
print(lst)
