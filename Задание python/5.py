import ifcopenshell


file_path = r"D:\IFC\Example_1.ifc"

model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")

min_width = 0

narrow_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)

    print("Дверь:", name, "Ширина", round(width), "Высота", height)