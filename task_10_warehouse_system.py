# task_10_warehouse_system.py 
"""
Система учёта склада строительных материалов
Контроль критических остатков, выдача материалов, расчёт стоимости
"""

from typing import Dict, Tuple

class Warehouse:
    """Складская система управления материалами"""
    
    def __init__(self, data: Dict):
        self.stock = data
    
    def get_total_value(self) -> float:
        """Общая стоимость всех материалов на складе"""
        return sum(item["quantity"] * item["price"] for item in self.stock.values())
    
    def get_most_expensive(self) -> Tuple[str, float]:
        """Находит самый дорогой материал (по общей стоимости)"""
        most = max(self.stock.items(), 
                   key=lambda x: x[1]["quantity"] * x[1]["price"])
        name = most[0]
        value = most[1]["quantity"] * most[1]["price"]
        return name, value
    
    def get_critical_items(self) -> Dict:
        """Возвращает материалы с количеством ниже минимального"""
        return {
            name: data
            for name, data in self.stock.items()
            if data["quantity"] < data["min_quantity"]
        }
    
    def issue_material(self, name: str, amount: int) -> bool:
        """
        Выдаёт указанное количество материала
        Возвращает True при успехе, False при ошибке
        """
        if name not in self.stock:
            print(f"Ошибка: Материал '{name}' не найден")
            return False
        
        if amount <= 0:
            print(f"Ошибка: Количество выдачи должно быть положительным")
            return False
        
        if self.stock[name]["quantity"] < amount:
            print(f"Ошибка: Недостаточно {name}")
            print(f"   Требуется: {amount}, Доступно: {self.stock[name]['quantity']}")
            return False
        
        old_qty = self.stock[name]["quantity"]
        self.stock[name]["quantity"] -= amount
        print(f"Выдано {amount} единиц '{name}'")
        print(f"  Остаток: {old_qty} -> {self.stock[name]['quantity']}")
        return True
    
    def display_table(self):
        """Выводит таблицу состояния склада"""
        print("\n" + "=" * 70)
        print("СИСТЕМА УЧЁТА СКЛАДА")
        print("=" * 70)
        
        print(f"{'Материал':<12} | {'Кол-во':>6} | {'Цена':>9} | {'Мин.':>5} | {'Стоимость':>12} | Статус")
        print("-" * 70)
        
        for name, data in self.stock.items():
            qty = data["quantity"]
            price = data["price"]
            min_qty = data["min_quantity"]
            value = qty * price
            
            status = "КРИТИЧ!" if qty < min_qty else "Норма"
            print(f"{name:<12} | {qty:>6} | {price:>9.2f} | {min_qty:>5} | {value:>12.2f} | {status}")
        
        print("-" * 70)
        
        total_value = self.get_total_value()
        most_expensive_name, most_expensive_value = self.get_most_expensive()
        critical = self.get_critical_items()
        
        print(f"ОБЩАЯ СТОИМОСТЬ: {total_value:>10.2f} руб")
        print(f"Самый дорогой: {most_expensive_name} ({most_expensive_value:>10.2f} руб)")
        
        if critical:
            print(f"КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical)} шт.):")
            for name, data in critical.items():
                print(f"   - {name}: {data['quantity']} < {data['min_quantity']}")
        else:
            print("Критических остатков нет")
        
        print("=" * 70)


def main():
    warehouse_data = {
        "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
        "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
        "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
        "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
        "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
    }
    
    warehouse = Warehouse(warehouse_data)
    
    warehouse.display_table()
    
    print("\n" + "СИМУЛЯЦИЯ ВЫДАЧИ МАТЕРИАЛА".center(70))
    print("-" * 70)
    
    warehouse.issue_material("Цемент", 25)
    warehouse.issue_material("Песок", 10)
    warehouse.issue_material("Гвозди", 5)
    
    warehouse.display_table()


if __name__ == "__main__":
    main()
