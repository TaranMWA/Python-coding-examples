import ExchangeRates

def GBP_TO_USD(amount):
    return amount * ExchangeRates.GBP_TO_USD

def GBP_TO_EUR(amount):
    return amount * ExchangeRates.GBP_TO_EUR

def GBP_TO_RUP(amount):
    return amount * ExchangeRates.GBP_TO_RUP

def GBP_TO_AUD(amount):
    return amount * ExchangeRates.GBP_TO_AUD

def GBP_TO_CAD(amount):
    return amount * ExchangeRates.GBP_TO_CAD

def GBP_TO_CHF(amount):
    return amount * ExchangeRates.GBP_TO_CHF

def GBP_TO_JPY(amount):
    return amount * ExchangeRates.GBP_TO_JPY

amount=int(input("Enter amount in GBP:"))

USD = GBP_TO_USD(amount)
EUR = GBP_TO_EUR(amount)
RUP = GBP_TO_RUP(amount)
AUD = GBP_TO_AUD(amount)
CAD = GBP_TO_CAD(amount)
CHF = GBP_TO_CHF(amount)
JPY = GBP_TO_JPY(amount)

print(f"USD: {USD}")
print(f"EUR: {EUR}")
print(f"RUP: {RUP}")
print(f"AUD: {AUD}")
print(f"CAD: {CAD}")
print(f"CHF: {CHF}")
print(f"JPY: {JPY}")
