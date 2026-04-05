C = float(input("°C: "))
F = C * 9/5 + 32
print(f"{C}°C = {round(F,1)}°F")

if C <= 0: s = "Лёд"
elif C >= 100: s = "Пар"
else: s = "Жидкость"
print("Состояние:", s)