numbers = input()
num_list = list(map(int, numbers.split()))
s = num_list[0]
v1 = num_list[1]
v2 = num_list[2]
v1_num = int(s / v1)
v2_num = (s - (v1_num * v1)) / v2

while v1_num >= 0 and v2_num % 1 == 0:
    if v1_num * v1 + v2_num * v2 == s:
        print(v1_num, int(v2_num))
        break
    v1_num -= 1
    v2_num = (s - (v1_num * v1)) / v2

else:
    print('Impossible')