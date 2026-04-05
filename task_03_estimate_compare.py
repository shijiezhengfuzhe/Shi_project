# task_03_estimate_compare.py 
"""
Конвертер температур и определитель состояния воды
Поддерживает шкалы Цельсия и Фаренгейта
"""

def celsius_to_fahrenheit(celsius):
    """Перевод из Цельсия в Фаренгейт"""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Обратный перевод (для полноты)"""
    return (fahrenheit - 32) * 5/9

def get_water_state(celsius):
    """
    Определяет состояние воды по температуре в °C
    Возвращает: 'Лёд', 'Жидкость', 'Пар'
    """
    if celsius <= 0:
        return "Лёд"
    elif celsius < 100:
        return "Жидкость"
    else:
        return "Пар"

def display_thermometer(celsius):
    """Графическое отображение температуры"""
    fahr = celsius_to_fahrenheit(celsius)
    state = get_water_state(celsius)
    
    print("\n" + "-" * 35)
    print(f"  {celsius:>6.1f} °C  =  {fahr:>6.1f} °F")
    print("-" * 35)
    print(f"  Состояние воды: {state}")
    print("-" * 35)


def main():
    print("ТЕМПЕРАТУРНЫЙ КОНВЕРТЕР")
    
    try:
        temp = float(input("Введите температуру в градусах Цельсия: "))
        display_thermometer(temp)
    except ValueError:
        print("Ошибка: введите числовое значение!")


if __name__ == "__main__":
    main()
