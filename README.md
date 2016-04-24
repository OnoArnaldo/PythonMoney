# PythonMoney
Basic money implementation

## Usage

It uses [Babel](http://babel.pocoo.org/en/latest/) library to get the string representation.
If you don't want to install Babel, remove the method `to_str`.

###### Basic usage
```
from money import Money

# Set default values
Money.default_currency = 'BRL'
Money.default_precision = 2

# Create instances
brl_10 = Money(1000)
brl_20 = Money(2000)
usd_10 = Money(1000, 2, 'USD')

# Operations
print (brl_10 + brl_20)  # Money(amount=3000, precision=2, currency="BRL")
print (brl_10 - brl_20)  # Money(amount=-1000, precision=2, currency="BRL")

print (brl_10 + 1500)    # Money(amount=2500, precision=2, currency="BRL")
print (brl_10 - 500)     # Money(amount=500, precision=2, currency="BRL")
print (brl_10 * 3)       # Money(amount=3000, precision=2, currency="BRL")

for money in brl_10.split(3):
    print (money)
      # Money(amount=333, precision=2, currency="BRL")
      # Money(amount=333, precision=2, currency="BRL")
      # Money(amount=334, precision=2, currency="BRL")

# Get float value
print (brl_10.to_float())      # 10.00

# Get string value based on locale
print (brl_10.to_str('pt_BR')) # R$10,00
```
