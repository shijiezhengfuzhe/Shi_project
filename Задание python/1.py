import ifcopenshell


file_path = r"D:\IFC\Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("Ifcwall")
print("Число стен:", len (walls))