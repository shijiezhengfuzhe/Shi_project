import argparse
import sys

class RoomCalculator:
    PAINT_PRICE_PER_SQM = 125.0

    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def compute(self):
        floor_area = round(self.length * self.width, 2)
        wall_area = round(2 * self.height * (self.length + self.width), 2)
        volume = round(self.length * self.width * self.height, 2)
        painting_cost = round(wall_area * self.PAINT_PRICE_PER_SQM, 2)
        return {
            "floor_area": floor_area,
            "wall_area": wall_area,
            "volume": volume,
            "painting_cost": painting_cost,
        }

    def display(self):
        res = self.compute()
        print("\n=== Результаты расчёта ===")
        print(f"Площадь пола: {res['floor_area']} м²")
        print(f"Площадь стен: {res['wall_area']} м²")
        print(f"Объём помещения: {res['volume']} м³")
        print(f"Стоимость покраски стен: {res['painting_cost']} руб")

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Ошибка: значение должно быть больше 0. Попробуйте снова.")
        except ValueError:
            print("Ошибка: введите число. Попробуйте снова.")

def main():
    parser = argparse.ArgumentParser(description="Расчёт параметров помещения и стоимости покраски стен.")
    parser.add_argument("-l", "--length", type=float, help="Длина помещения (м)")
    parser.add_argument("-w", "--width", type=float, help="Ширина помещения (м)")
    parser.add_argument("-ht", "--height", type=float, help="Высота помещения (м)")
    args = parser.parse_args()

    # Если все три аргумента переданы, используем их
    if args.length is not None and args.width is not None and args.height is not None:
        length, width, height = args.length, args.width, args.height
    else:
        print("Не все параметры указаны в командной строке. Будет использован интерактивный ввод.")
        print("Введите размеры помещения (в метрах):")
        length = get_positive_float("Длина: ")
        width = get_positive_float("Ширина: ")
        height = get_positive_float("Высота: ")

    room = RoomCalculator(length, width, height)
    room.display()

if __name__ == "__main__":
    main()