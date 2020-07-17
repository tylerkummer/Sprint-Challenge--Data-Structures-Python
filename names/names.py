import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# create an instance of Binary Search tree with an empty string as a placeholder to start the list
instance = BSTNode("")

# separate our for loops for better performance
# loop through our names_1 csv file
for name_1 in names_1:
    # with each element in names_1 we use our built in insert method into our BSTNode to compare later
    instance.insert(name_1)

# loop through our names_2 csv to go against our names_1 csv
for name_2 in names_2:
    # since names_1 csv is stored in our BSTNode we can use the built in contains method to compare names_1 to names_2
    if instance.contains(name_2):
        # if any instance of contains is true then we append our empty list duplicates with our name_2 since we can be sure it is in both names_1 and names_2
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
