# task_09_address_clean.py 
"""
Очистка и нормализация адресных строк
Удаление лишних пробелов, добавление пробелов после сокращений,
унификация разделителей
"""

import re

class AddressCleaner:
    """Класс для очистки и нормализации адресов"""
    
    ABBREVIATIONS = ['г', 'ул', 'д', 'пр', 'пер', 'пл']
    
    def __init__(self):
        self._patterns = {
            'trim_spaces': re.compile(r'\s+'),
            'abbrev_dot': re.compile(r'(' + '|'.join(self.ABBREVIATIONS) + r')\.'),
            'comma_spaces': re.compile(r'\s*,\s*'),
            'leading_trailing': re.compile(r'^\s+|\s+$')
        }
    
    def clean(self, address):
        """
        Основной метод очистки адреса
        """
        result = address
        
        result = self._patterns['leading_trailing'].sub('', result)
        result = self._patterns['trim_spaces'].sub(' ', result)
        result = self._patterns['abbrev_dot'].sub(r'\1. ', result)
        result = self._patterns['comma_spaces'].sub(', ', result)
        result = self._patterns['trim_spaces'].sub(' ', result)
        
        return result
    
    def compare_and_print(self, original):
        """Выводит сравнение исходного и очищенного адреса"""
        cleaned = self.clean(original)
        print(f"ДО:   '{original}'")
        print(f"ПОСЛЕ: '{cleaned}'")
        print()


def main():
    addresses = [
        " г. Москва, ул. Ленина, д. 10  ",
        "г.Казань,ул.Баумана,д.15",
        " г. Санкт-Петербург, ул. Невский, д. 100  "
    ]
    
    cleaner = AddressCleaner()
    
    print("=" * 50)
    print("НОРМАЛИЗАЦИЯ АДРЕСОВ")
    print("=" * 50)
    print()
    
    for i, addr in enumerate(addresses, 1):
        print(f"--- Адрес #{i} ---")
        cleaner.compare_and_print(addr)
    
    print("=" * 50)
    print("Очистка завершена")


if __name__ == "__main__":
    main()
