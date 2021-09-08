# Calculate average from a list

hlist = input("Please enter a number of different values: ")

data = hlist.split(" ") # creates a list

# total = sum(data)
# average = total / len(data)
# print average
'''USING THE FOR LOOP'''
total = 0
num_items = 0

for value in data:
    value = int(value)              # covert each number into an int
    total += value
    num_items += 1
# then divide by number of items, round of to 2 decimal places

average = round(total / num_items , 0)

print(f"The average is: {average}")

