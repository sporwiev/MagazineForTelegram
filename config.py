import datetime
from dataclasses import dataclass

admin_ids = [10101,913910903,1129702247,706999827,1474775392]
#,913910903
#1474775392,1129702247,5453553454,4565664646,76765756756,
def get_admins(message):
    for i in admin_ids:

        if i == message:
            return i

def get_pledlog():
    if int(datetime.date.today().day) % 7 == 0:
        return '7% на всё, вместо стандарных 5%'
    elif int(datetime.date.today().day) % 7 == 1:
        return '10% на одноразки'
    elif int(datetime.date.today().day) % 7 == 2:
        return '10% на кальянную продукцию'
    elif int(datetime.date.today().day) % 7 == 3:
        return '10% на жидкости'
    elif int(datetime.date.today().day) % 7 == 4:
        return '15% на под системы'
    elif int(datetime.date.today().day) % 7 == 5:
        return '20% скидка при покупке двух товаров'
    elif int(datetime.date.today().day) % 7 == 6:
        return '7% на всё, вместо стандарных 5%'
@dataclass
class Config:
    token: str = '6472908781:AAEDVrXElu2RKZLWDhQ47rAKfTvxtEhiM7o'

