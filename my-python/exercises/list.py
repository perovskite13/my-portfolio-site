#Q1
foods = ["orange", "apple", "banana", "strawberry", "grape", "blueberry", 
["carrot", "cauliflower", "pumpkin"], 
"passionfruit", "mango", "kiwifruit"]
print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[-3:])
print(foods[:3])
print(foods[6][-1]) #get sublist

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
print(names)

#Q4
string = input("enter a string: ")
s = string.split(" ")
print(len(s), s)

sls = list(string)
print(len(sls), sls)



