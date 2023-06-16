def consumption_tax(price, tax):
  return price * (1+tax/100)

print(consumption_tax(100, 10))
