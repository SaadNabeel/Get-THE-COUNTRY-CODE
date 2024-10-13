country = {'India': '0091', 'Pakistan': '0092', 'Nepal': '00977', 'USA': '0025'}

print('Displaying country code')

print('India:', country.get('India', 'Not found'))
print('Pakistan:', country.get('Pakistan', 'Not found'))
print('Nepal:', country.get('Nepal', 'Not found'))
print('Argentina:', country.get('Argentina', 'Not found'))
