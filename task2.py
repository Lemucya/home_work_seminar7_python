"""
2) Реализовать класс Road (дорога), в котором определить атрибуты: length
(длина), width (ширина). Значения данных атрибутов должны передаваться при
создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self._length
        wid = self._width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(
            f"Масса асфальта:\n {leng} м * {wid} м * {w} кг * {dep} см = ",
            total, "т")


r = Road(20, 5000, 25, 5)
r.mass()

"""
вариант преподавателя:

class Road:
    weight = 25
    thickness = 0.05
    
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def calc(self):
        res = (self._length * self._width * Road.weight * Road.thickness) / 1000
        print(f'Потребуется {res} тонн')
        
r_obj = Road(20, 5000)
r_obj.calc()
"""
