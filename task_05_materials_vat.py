p = float(input("Цена: "))
q = int(input("Кол-во: "))
s = p * q

if s < 1000: d = 0
elif s <= 5000: d = 0.05
else: d = 0.1

print(f"Сумма: {s}")
print(f"Скидка: {d*100}%")
print(f"Итого: {s*(1-d):.2f}")