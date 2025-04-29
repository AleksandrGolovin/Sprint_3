import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # Список товаров в чеке
    @property
    def name_items(self):
        return self.__name_items
    
    # Количество товаров в чеке
    @property
    def number_items(self):
        return self.__number_items

    # Добавить товар в чек, если валидное наименование и есть в списке товаров    
    def add_item_to_cheque(self, name):
        try:
            if (len(name) == 0) or (len(name) > 40):
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            if not name in self.__item_price.keys():
                raise KeyError('Позиция отсутствует в товарном справочнике')
        except Exception as e:
            print(e)
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    # Удалить товар из чека по наименованию
    # В постановке задачи то check, то cheque...
    def delete_item_from_check(self, name):
        try:
            if not name in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
        except Exception as e:
            print(e)
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1
    
    # Посчитать сумму чека и сумму чека со скидкой
    def check_amount(self):
        total = list(map(lambda name: self.__item_price[name], self.__name_items))
        if self.__number_items > 10:
            return sum(total) * 0.9
        return sum(total)

    # Сумма НДС на товары в чеке со ставкой 20%
    def twenty_percent_tax_calculation(self):
        tax_rate = 20
        twenty_percent_tax = list(filter(lambda name: self.__tax_rate[name] == tax_rate, self.__name_items))
        total = list(map(lambda name: self.__item_price[name], twenty_percent_tax))
        if self.__number_items > 10:
            return sum(total) * 0.9 * (tax_rate / 100)
        return sum(total) * (tax_rate / 100)
    
    # Сумма НДС на товары в чеке со ставкой 10%
    def ten_percent_tax_calculation(self):
        tax_rate = 10
        ten_percent_tax = list(filter(lambda name: self.__tax_rate[name] == tax_rate, self.__name_items))
        total = list(map(lambda name: self.__item_price[name], ten_percent_tax))
        if self.__number_items > 10:
            return sum(total) * 0.9 * (tax_rate / 100)
        return sum(total) * (tax_rate / 100)
    
    # Общая сумма НДС
    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
    
    # Номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number: int = None) -> str:
        try:
            if not type(telephone_number).__name__ == 'int':
                raise ValueError('Необходимо ввести цифры')
            if len(str(telephone_number))>10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
        except Exception as e:
            return e
        else:
            return f'+7{telephone_number}'
    
    # Получить текущую дату и время
    @staticmethod
    def get_date_and_time() -> list[str]:
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]
        for date_attr, date_lambda in date:
            date_and_time.append(f'{date_attr}: {date_lambda(now)}')
        return date_and_time

collector = OnlineSalesRegisterCollector()

collector.add_item_to_cheque("чипсы")
collector.add_item_to_cheque("кола")
collector.add_item_to_cheque("печенье")
collector.add_item_to_cheque("молоко")
collector.add_item_to_cheque("кефир")
collector.add_item_to_cheque("чипсы")
collector.add_item_to_cheque("кола")
collector.add_item_to_cheque("печенье")
collector.add_item_to_cheque("молоко")
collector.add_item_to_cheque("кефир")
collector.add_item_to_cheque("кефир")

print(f'Товары в чеке: {collector.name_items}')
print(f'Всего в чеке товаров: {collector.number_items}')
print(f'Сумма чека: {collector.check_amount()}')
print(f'В том числе НДС: {collector.total_tax()}. Состоит из:')
print(f'- 10% НДС: {collector.ten_percent_tax_calculation()}')
print(f'- 20% НДС: {collector.twenty_percent_tax_calculation()}')
print(f'Телефон покупателя: {OnlineSalesRegisterCollector.get_telephone_number(8005553535)}')
print(f'Текущая дата и время: {OnlineSalesRegisterCollector.get_date_and_time()}')