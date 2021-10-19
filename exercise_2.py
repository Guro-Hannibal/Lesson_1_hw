time_in_seconds = int(input('Введите время в секундах - '))
hours = time_in_seconds // 60 // 60
minutes = time_in_seconds // 60 - hours * 60
seconds = time_in_seconds - minutes * 60 - hours * 3600
print(hours, minutes, seconds, sep=':')
""" print('{0:.1f}'.format(minutes)) """
