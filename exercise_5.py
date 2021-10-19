profit = int(input('Выручка - '))
costs = int(input('Издержки - '))
is_profit = False
profitability = None
profit_by_employer = None
employers = None
if profit > costs:
    is_profit = True
    profitability = (profit - costs) / profit
    employers = int(input('Сотрудники - '))
    profit_by_employer = profit / employers
print(is_profit)
print(profitability)
print(profit_by_employer)
