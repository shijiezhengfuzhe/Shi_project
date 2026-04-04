def calculate_room_params(length: float, width: float, height: float) -> dict:
    """
    Рассчитывает геометрические параметры помещения и стоимость покраски стен.

    Параметры:
        length (float): Длина помещения (метры)
        width (float): Ширина помещения (метры)
        height (float): Высота помещения (метры)

    Возвращает:
        dict: Словарь с результатами (все значения округлены до 2 знаков):
            - floor_area: Площадь пола (м²)
            - wall_area: Площадь стен (м²)
            - volume: Объём помещения (м³)
            - painting_cost: Стоимость покраски стен (руб)
    """
    # Расчёт параметров
    floor_area = length * width
    wall_area = 2 * height * (length + width)   # Четыре стены, без учёта потолка и пола
    volume = length * width * height
    painting_cost = wall_area * 125             # 125 руб/м²

    # Округление до 2 знаков
    result = {
        "floor_area": round(floor_area, 2),
        "wall_area": round(wall_area, 2),
        "volume": round(volume, 2),
        "painting_cost": round(painting_cost, 2)
    }
    return result


# Пример использования
if __name__ == "__main__":
    # Здесь можно изменить значения для тестирования
    length = 5.0
    width = 4.0
    height = 3.0

    params = calculate_room_params(length, width, height)

    print("Результаты расчёта:")
    print(f"Площадь пола: {params['floor_area']} м²")
    print(f"Площадь стен: {params['wall_area']} м²")
    print(f"Объём помещения: {params['volume']} м³")
    print(f"Стоимость покраски стен: {params['painting_cost']} руб")