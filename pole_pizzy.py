
'''Pizzeria oferuje pizze:

small - promień 22 cm, cena, 11.50

big - promień 27 cm, cena 15.60

family - promień 38cm, cena 22.00
Oblicz powierzchnię kazdej pizzy w metrach kwadratowych i cene pizzy za metr kwadratowy'''

import math

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22
pole_small = round(math.pi*math.pow(small_pizza_r/2/100, 2), 4)
pole_big = round(math.pi*math.pow(big_pizza_r/2/100, 2), 4)
pole_family = round(math.pi*math.pow(family_pizza_r/2/100, 2), 4)
price_small_mkw = small_pizza_price/pole_small
print(price_small_mkw)

print('Pole powierzchni Small pizza to ' +
      str(pole_small) + ' metrów kwadratowych.')
print('Pole powierzchni big pizza to ' +
      str(pole_big) + ' metrów kwadratowych.')
print('Pole powierzchni family pizza to ' +
      str(pole_family) + ' metrów kwadratowych.')
print('Cena metra kwadratowego small pizzy wynosi ' +
      str(round(small_pizza_price/pole_small, 2))+' zł.')
print('Cena metra kwadratowego big pizzy wynosi ' +
      str(round(big_pizza_price/pole_big, 2))+' zł.')
print('Cena metra kwadratowego family pizzy wynosi ' +
      str(round(family_pizza_price/pole_family, 2))+' zł.')
