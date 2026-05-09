import ifcopenshell


file_path = r"D:\IFC\Example_1.ifc"

model = ifcopenshell.open(file_path)


storeys = model.by_type("IfcBuildingStorey")
# walls
# doors
# window

print("Схема IFC:", model.schema)
print("Этажей:", len(storeys))