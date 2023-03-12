# Python program to demonstrate adding the elements into the list
Sample_list=[]
print("The list before adding the elements into it",Sample_list)
Sample_list.append(1)
Sample_list.append(2)
print("The list after adding the elements into it using append method",Sample_list)
Sample_list.append((5,6))
print("The list after adding the tupple into it using append method",Sample_list)
Sample_list.append({1:1})
print("The list after adding the dictionary into it using append method",Sample_list)
for i in range(12,23):
    Sample_list.append(i)
print("The list after adding the elements into it using append method and range method",Sample_list)
#using insert method
Sample_list.insert(2,4)
print("The list before adding the elements into it using insert method",Sample_list)
Sample_list.insert(2,(6,7))
print("The list after adding the elements into it using insert method",Sample_list)
#using extend method
Sample_list.extend({1:4,'eee':'fff',33:666})
print("The list after adding the elements into it using extend method",Sample_list)
Sample_list.reverse()
print("The reveres list is",Sample_list)
Sample_list.__reversed__()
print("The revered list is",Sample_list)

# List Comprehension:

odd_square=[]
NewList=[x**2 for x in range (1,100) if x%2==1]
print(NewList)


