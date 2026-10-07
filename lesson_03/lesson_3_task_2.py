from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "M11", "+79994538757"),
    Smartphone("Samsung", "galaxy7", "+79397456322"),
    Smartphone("Honor", "H56", "+79334445566"),
    Smartphone("Poco", "F8", "+79253459911"),
    Smartphone("Apple", "A10", "+79293337612")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
