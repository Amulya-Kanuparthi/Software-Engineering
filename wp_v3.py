# -*- coding: utf-8 -*-
"""WP V3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HZtSmlRYSZYbvTz5-7rN7qY_1YHrkjjN
"""

variable = {}
with open('/content/weatherfile.txt', 'r') as file:
  for line in file:
    name, value = line.replace(' ', '').split('=')
    variable[name] = int(value)
W=(0.5)*(variable['T']**2)-(0.2)*variable['H']+(0.1)*variable['w']-15
print(W)
if W>300:
  print("Sunny")
elif 200<W<=300:
  print("Cloudy")
elif 100<W<=200:
  print("Rainy")
else:
  print("Stormy")