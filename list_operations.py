
my_list = [3, 1, 2]


my_list.append(4)
print( my_list)  


my_list.extend([5, 6])
print("After extend([5, 6]):", my_list)  


my_list.insert(2, 10)
print("After insert(2, 10):", my_list)  


my_list.remove(1)
print("After remove(1):", my_list)

popped = my_list.pop(3)
print("After pop(3):", my_list)

temp_list = my_list.copy()       
my_list.clear()
print("After clear():", my_list)   


my_list = temp_list.copy()


print("Index of 10:", my_list.index(10))  


print("Count of 5:", my_list.count(5))    


my_list.sort()
print("After sort():", my_list)

my_list.reverse()
print("After reverse():", my_list)

new_list = my_list.copy()
print("Copied list:", new_list)          
