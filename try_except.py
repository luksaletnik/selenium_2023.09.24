

price = input('Please enter a price: ')

try:
    price = float(price)
    print('Ok')

except:
    print('Type:', type(price))
    price = 0
    print('The price is no valid! Try again!')

score = price * 3.3

print(score)
