import ifcopenshell
import ifcopenshell.util.element

file_path = r"D:\IFC\Example_1.ifc"
model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")
min_width = 900   # минимальная ширина

# Фильтрация широких дверей
wide_doors = []
for door in doors:
    width = getattr(door, "OverallWidth", None)
    if width is not None and width >= min_width:
        wide_doors.append(door)

print("Всего дверей:", len(doors))
print("Широких дверей (ширина >= {}):".format(min_width), len(wide_doors))

if wide_doors:
    # Создание новой пустой модели
    new_model = ifcopenshell.file(schema=model.schema)
    
    # Создание простого объекта IfcDoor для каждой широкой двери
    for door in wide_doors:
        # Получение атрибутов исходной двери
        global_id = door.GlobalId
        name = door.Name
        width_val = getattr(door, "OverallWidth", None) or 0
        height_val = getattr(door, "OverallHeight", None) or 0
        
        # Создание IfcDoor в новой модели
        new_door = new_model.create_entity(
            "IfcDoor",
            GlobalId=global_id,
            Name=name,
            OverallWidth=width_val,
            OverallHeight=height_val
        )
       
    
    # Сохранение новой модели
    out_path = r"D:\IFC\_doors_wide.ifc"
    new_model.write(out_path)
    print(f"Создан файл с {len(wide_doors)} дверями: {out_path}")
    
    # Проверка: повторное открытие и подсчёт дверей
    verify = ifcopenshell.open(out_path)
    print("Проверка: в новом файле дверей =", len(verify.by_type("IfcDoor")))
else:
    print("Нет широких дверей.")