num = int(input('Или роллы - '))
num_digit_count = num
i = num
y = 0
max_digit = 0
""" while num_digit_count != 0:
    num_digit_count = num_digit_count // 10
    i += 1
else:
    num_digit_count = i """
while num > 10:
    i = num % 10
    num //= 10
    if i > max_digit:
        max_digit = i
print(max_digit)
