'''
1- random.randint
2- put input in list
3- for ele in list:
    convert the int into str and make a loop:  while i != ele:  str =+ str
        print(ele:str)
'''

n = input()
digits_list = [int(d) for d in str(n)]
for ele in digits_list:
    if ele == 0:
        print('0: ')
    else:
        num_str = str(ele)
        for i in range(ele - 1):
            num_str += str(ele)
        print('%i: %s' % (ele, num_str))

