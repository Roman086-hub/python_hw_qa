from address import Address
from mailing import Mailing

to_address = Address("143430", "Nahabino",
                     "Sovetskaya", "44", "33")
from_address = Address("384574", "Moh",
                       "Lenina", "2", "12")
mailing = Mailing(to_address, from_address, cost=43, track=776)
print(f"Отправление {mailing.track} из {mailing.from_address} в"
      f" {mailing.to_address}. Стоимость {mailing.cost} рублей")
