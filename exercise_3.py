num = input('Хочу пиццу - ')
i = 0
str_num = ''
result = 0
while i < int(num):
    str_num += num
    result += int(str_num)
    i += 1
print(result)
