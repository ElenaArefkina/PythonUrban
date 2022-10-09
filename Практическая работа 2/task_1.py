# -*- coding: utf-8 -*-
"""Практика 2. Задание 1.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18kL3FDsOR7x9ze074XF2AEmclX4rWKkg
"""

class GreenZoneIndex:
    def __init__(self, territory_name: str, territory_area: int, green_zones: list):
        """
        :param territory_name: Название территории
        :param territory_area: Площадь территории
        :param green_zones: Список площадей парков
        """
        # TODO все аргументы конструктора записать в атрибуты экземпляра класса

        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones
       
        # индекс озеленения
        self.green_index = round(self.calculate_green_index(), 2)
        # TODO посчитать индекс озеленения с помощью метода calculate_green_index

    def calculate_green_index(self):
        """
        Метод для вычисления индекса озеленения.

        Индекс рассчитывается как отношение площади всех парков к площади территории
        """
        
        # TODO посчитать индекс озеленения с атрибутов экземпляра класса

        green_index = (sum(self.green_zones) / self.territory_area)*100
        
        return green_index
        # Задаем переменные
territory_name = "Пушкин"
territory_area = 28676
green_zones = [302, 487, 420, 325, 471, 363, 404]
# TODO Создать экземпряр класса и с помощью его атрибутов распечатать индекс озеленения в процентах до 2 знака после запятой.

pushkin_green = GreenZoneIndex(territory_name, territory_area, green_zones)

print(f"Индекс озеленения территории {pushkin_green.territory_name} равен {pushkin_green.green_index} %")
# Ожидаемый ответ Индекс озеленения территории Пушкин равен 9.67%