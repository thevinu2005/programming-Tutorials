file = open('shopping.txt','r')
lines = file.readline()
for line in lines:
    words = line.split()
    number = int(words[1])
    cost = float(words[2])
    print(f'item {words[0]} = total {number * cost}')