'''
1- n = int(input()
2- numbers = input()    1 2 3 2
3- put numbers in list
4- for ele in list count in list[index(ele):] these: ele+1 and ele-1
5- print(count)
'''

n = int(input())
numbers = input()
num_list = list(map(int, numbers.split()))
counter = 0
for ele in num_list:
    index = num_list.index(ele)
    num_list = num_list[index:]
    countplus = num_list.count(ele+1)
    countminus = num_list.count(ele-1)
    counter = counter+countplus+countminus

print(counter)


#### age error dad: if n == len(num_list):
    #baqieye code