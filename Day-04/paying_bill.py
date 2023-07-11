import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

nameAsCSV = input("Give me everbody's names,seperated by a comma: ")
names = nameAsCSV.split(",")

# x = len(names) - 1
#
# paying_person = random.randint(0, x)
# print(names[paying_person]+" is going to buy meal today!")

paying_person = random.choice(names)
print(paying_person+" is going to buy meal today!")
