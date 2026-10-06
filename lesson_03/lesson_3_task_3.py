from address import Address
from mailing import Mailing

to_add = Address("143430", "Nahabino", "Sovetskaya", "44", "33")
from_add = Address("384574", "Moh", "Lenina", "2", "12")
mail = Mailing(to_address = to_add, from_address = from_add, cost=43, track=776)
print(f"Отправление {mail.track} из {mail.from_address} в {mail.to_address}. Стоимость {mail.cost} рублей")