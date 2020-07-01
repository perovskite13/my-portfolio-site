#Q1 

i = 0
s = 0
i = input("give me a number: ")
while i != "":
    s = s + int(i)
    print(s)   
    i = input("give me a number: ")
i = 0
print(i)


#Q2
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]
for item in mailing_list:
    print(f"{item[0]} : {item[1]}")

#Q3
names = []
while len(names) < 3:
    nm = input("3 names :")
    names.append(nm)
for name in names:
    print(name)

#Q4
groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

cost = []
total = 0
for food in groceries:
    order = int(input(f"how many {food[0]} did you buy?:"))
    cost.append(food[1]*order)
    total = total+(food[1]*order)
#print(cost)
#print(total)

print("======Izzy's Food Emporium=====")
for i in range(len(groceries)):
    print(f"{groceries[i][0]}   ${cost[i]:.2f}")
print("===============================")
print(f"          ${total}")