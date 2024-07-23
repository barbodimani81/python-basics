n = int(input())
password = (input())
password_list = [int(d) for d in str(password)]
j = 0
counter = 0
for i in range(n):
    charkhune = (input())
    charkhune_list = [int(d) for d in str(charkhune)]
    k = password_list[j]
    index = charkhune_list.index(k)
    if index <= 4:
        counter += index
    elif index >= 5:
        index = 9 - index
        counter += index
    j += 1
print(counter)