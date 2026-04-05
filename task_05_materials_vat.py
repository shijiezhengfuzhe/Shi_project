# task_05_materials_vat.py 
"""
Калькулятор скидок с прогрессивной шкалой
Выводит все этапы расчёта
"""

DISCOUNT_BRACKETS = [
    (0, 0.00),
    (1000, 0.05),
    (5000, 0.10)
]

def get_discount_rate(amount):
    """
    Определяет процент скидки в зависимости от суммы
    """
    for threshold, rate in reversed(DISCOUNT_BRACKETS):
        if amount >= threshold:
            return rate
    return 0.0

def format_currency(value):
    """Форматирует число как рубли"""
    return f"{value:,.2f} руб".replace(",", " ")

def main():
    print("КАЛЬКУЛЯТОР СКИДОК")
    print("=" * 40)
    
    price = float(input("Цена за единицу (руб): "))
    quantity = int(input("Количество: "))
    
    subtotal = price * quantity
    discount_rate = get_discount_rate(subtotal)
    discount_amount = subtotal * discount_rate
    final_amount = subtotal - discount_amount
    
    print("\n" + "-" * 40)
    print("ЭТАПЫ РАСЧЁТА")
    print("-" * 40)
    print(f"1. Стоимость без скидки:     {format_currency(subtotal)}")
    print(f"2. Применённая скидка:       {discount_rate * 100:.0f}%")
    print(f"3. Сумма скидки:             {format_currency(discount_amount)}")
    print(f"4. ИТОГО К ОПЛАТЕ:           {format_currency(final_amount)}")
    print("-" * 40)


if __name__ == "__main__":
    main()
