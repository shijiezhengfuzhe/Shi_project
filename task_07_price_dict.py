# task_07_price_dict.py
"""
Прайс-лист материалов
Управление словарём: добавление, изменение, удаление, статистика
"""

class PriceList:
    """Класс для управления ценами на материалы"""
    
    def __init__(self, initial_prices=None):
        self.prices = initial_prices if initial_prices else {}
    
    def add_item(self, name, price):
        """Добавляет новый материал"""
        self.prices[name] = price
        print(f"  + Добавлен: {name} = {price:.2f} руб")
    
    def update_item(self, name, multiplier):
        """Изменяет цену с коэффициентом"""
        if name in self.prices:
            old = self.prices[name]
            self.prices[name] = round(old * multiplier, 2)
            print(f"  Изменён: {name} {old:.2f} -> {self.prices[name]:.2f} руб (+{(multiplier-1)*100:.0f}%)")
    
    def remove_item(self, name):
        """Удаляет материал"""
        if name in self.prices:
            removed = self.prices.pop(name)
            print(f"  Удалён: {name} (было {removed:.2f} руб)")
    
    def average_price(self):
        """Вычисляет среднюю цену"""
        if not self.prices:
            return 0.0
        return sum(self.prices.values()) / len(self.prices)
    
    def display(self):
        """Выводит текущий прайс-лист"""
        print("\n" + "-" * 40)
        print("ТЕКУЩИЙ ПРАЙС-ЛИСТ")
        print("-" * 40)
        for name, price in sorted(self.prices.items()):
            print(f"  {name:<15} {price:>10.2f} руб")
        print(f"  {'СРЕДНЯЯ':<15} {self.average_price():>10.2f} руб")
        print("-" * 40)


def main():
    initial = {
        "Кирпич": 12.50,
        "Цемент": 450.00,
        "Песок": 800.00,
        "Бетон": 4200.00,
        "Арматура": 48000.00
    }
    
    pl = PriceList(initial)
    print("УПРАВЛЕНИЕ ПРАЙС-ЛИСТОМ")
    
    print("\nОперация 1: Добавление 2 материалов")
    pl.add_item("Доска", 350.00)
    pl.add_item("Гвозди", 1.50)
    
    print("\nОперация 2: Изменение цены (+10%)")
    pl.update_item("Цемент", 1.10)
    
    print("\nОперация 3: Удаление материала")
    pl.remove_item("Песок")
    
    pl.display()


if __name__ == "__main__":
    main()
