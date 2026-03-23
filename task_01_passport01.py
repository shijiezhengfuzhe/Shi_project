student_name = "Ши Юэ"
group_number = "3140801/52501"
project_name = "回家"
floors = 8
height = 25.3
is_residential = True
construction_year = 2003

#Формирование словаря с данными объекта
building_passport = {
    "Составитель": student_name,
    "Группа": group_number,
    "Объект": project_name,
    "Этажность": f"{floors} этажей",
    "Высота": f"{height} м",
    "Тип": "Жилой" if is_residential else "Нежилой",
    "Год постройки": construction_year
}

# Вывод в читаемом виде с использованием заголовков
print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
for key, value in building_passport.items():
    print(f"{key}: {value}")
print("=====================================")
# Местоположение: № 2, район Чаоян, Шанхай
# Обоснование выбора: Знаковое здание
