# task_06_materials_catalog.py
"""
Каталог материалов
Демонстрация операций со списками: индексация, срезы, добавление, удаление
"""

def display_list_info(lst, title="Список"):
    """Выводит информацию о списке"""
    print(f"\n{title}:")
    print(f"  Элементы: {lst}")
    print(f"  Длина: {len(lst)}")

def get_first_last_middle(lst):
    """Возвращает первый, последний и средний(е) элементы"""
    first = lst[0]
    last = lst[-1]
    
    mid_idx = len(lst) // 2
    if len(lst) % 2 == 0:
        middle = lst[mid_idx-1:mid_idx+1]
    else:
        middle = [lst[mid_idx]]
    
    return first, last, middle

def main():
    materials = ["Кирпич", "Цемент", "Песок", "Бетон", "Арматура"]
    display_list_info(materials, "Исходный каталог")
    
    first, last, middle = get_first_last_middle(materials)
    print(f"\nДоступ к элементам:")
    print(f"  Первый: {first}")
    print(f"  Последний: {last}")
    print(f"  Средний(е): {middle}")
    
    materials.append("Доска")
    materials.append("Гвозди")
    display_list_info(materials, "После добавления")
    
    removed = materials.pop(1)
    print(f"\nУдалён элемент: '{removed}' (второй по счёту)")
    
    display_list_info(materials, "Итоговый каталог")
    
    print("\n" + "=" * 40)
    print(f"Всего материалов в каталоге: {len(materials)}")


if __name__ == "__main__":
    main()
