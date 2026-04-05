# task_04_foundation_load.py 
"""
Определитель рабочего графика
По номеру дня недели выводит название и режим работы
"""

from enum import IntEnum

class Weekday(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

DAY_NAMES = {
    Weekday.MONDAY: "Понедельник",
    Weekday.TUESDAY: "Вторник",
    Weekday.WEDNESDAY: "Среда",
    Weekday.THURSDAY: "Четверг",
    Weekday.FRIDAY: "Пятница",
    Weekday.SATURDAY: "Суббота",
    Weekday.SUNDAY: "Воскресенье"
}

WORK_SCHEDULE = {
    "work_start": "08:00",
    "work_end": "17:00",
    "break_start": "12:00",
    "break_end": "13:00"
}

def is_workday(day_num):
    """Возвращает True для рабочих дней (ПН-ПТ)"""
    return day_num in range(1, 6)

def get_schedule_message(day_num):
    """Формирует сообщение о режиме работы"""
    if is_workday(day_num):
        return f"Рабочий день — начало смены в {WORK_SCHEDULE['work_start']}"
    else:
        return "Выходной день — отдых"

def main():
    print("=" * 40)
    print("КАЛЕНДАРЬ РАБОЧЕГО ГРАФИКА")
    print("=" * 40)
    
    try:
        day_number = int(input("Введите номер дня недели (1-7): "))
        
        if day_number < 1 or day_number > 7:
            print("\n[ОШИБКА] Число должно быть от 1 до 7!")
            return
        
        day_name = DAY_NAMES[Weekday(day_number)]
        schedule = get_schedule_message(day_number)
        
        print("\n" + "-" * 35)
        print(f"  {day_name}")
        print(f"  {schedule}")
        print("-" * 35)
        
    except ValueError:
        print("\n[ОШИБКА] Введите целое число!")


if __name__ == "__main__":
    main()
