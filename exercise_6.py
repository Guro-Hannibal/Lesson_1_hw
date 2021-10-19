a = int(input('start - '))
b = int(input('desired result - '))
i = 1
print(f'{i}-й день: {a}')
while a <= b:
    a *= 1.1
    i += 1
    print(f'{i}-й день: {a}')
print(f'На {i} день результат составит не менее {b} км')
