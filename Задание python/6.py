import ifcopenshell

# Открытие модели
file_path = r"D:\IFC\Example_1.ifc"
model = ifcopenshell.open(file_path)

# Получение всех стен
walls = model.by_type("IfcWall")
print("Число стен:", len(walls))

if walls:
    first_wall = walls[0]
    
    # Вывод оригинального имени
    print("Оригинальное Name:", first_wall.Name)
    
    # Изменение имени (прямое присваивание)
    first_wall.Name = "MODIFIED_" + (first_wall.Name or "Unnamed")
    
    # Сохранение в новый IFC-файл
    new_path = r"D:\IFC\_modified.ifc"
    model.write(new_path)
    print(f"Сохранено в: {new_path}")
    
    # Повторное открытие для проверки
    new_model = ifcopenshell.open(new_path)
    new_walls = new_model.by_type("IfcWall")
    print("Проверка: новое Name =", new_walls[0].Name)
else:
    print("Стены не найдены.")