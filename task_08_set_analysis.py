# task_08_set_analysis.py 
"""
Анализ поставок материалов от трёх подрядчиков
Использование операций над множествами
"""

def analyze_suppliers(s1, s2, s3):
    """
    Выполняет полный анализ трёх множеств материалов
    Возвращает словарь с результатами
    """
    set1, set2, set3 = set(s1), set(s2), set(s3)
    
    results = {
        "all_unique": set1 | set2 | set3,
        "common_all": set1 & set2 & set3,
        "only_first": set1 - set2 - set3,
        "only_second": set2 - set1 - set3,
        "only_third": set3 - set1 - set2,
        "exactly_two": (set1 & set2) | (set1 & set3) | (set2 & set3) - (set1 & set2 & set3)
    }
    return results

def print_analysis_report(results):
    """Выводит отформатированный отчёт"""
    print("\n" + "=" * 50)
    print("АНАЛИЗ МАТЕРИАЛОВ ПОДРЯДЧИКОВ")
    print("=" * 50)
    
    print("\nВсе уникальные материалы:")
    print(f"   {sorted(results['all_unique'])}")
    
    print("\nОбщие для всех трёх подрядчиков:")
    print(f"   {sorted(results['common_all']) if results['common_all'] else '— нет —'}")
    
    print("\nТолько у первого подрядчика:")
    print(f"   {sorted(results['only_first']) if results['only_first'] else '— нет —'}")
    
    print("\nРовно у двух подрядчиков:")
    print(f"   {sorted(results['exactly_two']) if results['exactly_two'] else '— нет —'}")
    
    print("\n" + "=" * 50)


def main():
    supplier1 = ["Кирпич", "Цемент", "Песок", "Гвозди", "Шурупы"]
    supplier2 = ["Цемент", "Песок", "Бетон", "Доска", "Гвозди"]
    supplier3 = ["Песок", "Бетон", "Арматура", "Гвозди", "Шурупы"]
    
    print("Исходные данные:")
    print(f"  Подрядчик 1: {supplier1}")
    print(f"  Подрядчик 2: {supplier2}")
    print(f"  Подрядчик 3: {supplier3}")
    
    results = analyze_suppliers(supplier1, supplier2, supplier3)
    print_analysis_report(results)
    
    print(f"\nСтатистика:")
    print(f"  Всего уникальных материалов: {len(results['all_unique'])}")
    print(f"  Материалов у всех трёх: {len(results['common_all'])}")
    print(f"  Материалов ровно у двух: {len(results['exactly_two'])}")


if __name__ == "__main__":
    main()
