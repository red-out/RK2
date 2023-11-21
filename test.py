from main1 import *
import unittest


# Тестирование класса «Деталь»
class TestComponent(unittest.TestCase):
    def test_component_creation(self):
        test_comp = Component(11, "Тормозные колодки", 12000, 7)
        self.assertEqual(test_comp.id, 11)
        self.assertEqual(test_comp.name, "Тормозные колодки")
        self.assertEqual(test_comp.price, 12000),
        self.assertEqual(test_comp.fabric_id, 7)


# Тестирование класса «Производитель»
class TestFabric(unittest.TestCase):
    def test_fabric_creation(self):
        test_fabric = Fabric(10, "АВТОВАЗ")
        self.assertEqual(test_fabric.id, 10)
        self.assertEqual(test_fabric.name, "АВТОВАЗ")


# Тестирование класса для реализация связи «Многие ко многим»
class TestFabricComponent(unittest.TestCase):
    def test_map_creation(self):
        test_map = FabricComponent(1, 3)
        self.assertEqual(test_map.fabric_id, 1)
        self.assertEqual(test_map.component_id, 3)


class TestMainFunctions(unittest.TestCase):
    # Генерация тестовых данных
    def setUp(self):
        self.components = [
            Component(1, "Тормозные колодки", 12000, 1),
            Component(2, "Фары", 5000, 1),
            Component(3, "Заднее крыло", 10000, 2),
            Component(4, "Генератор", 15000, 3),
            Component(5, "Аккумулятор", 8000, 3),
            Component(6, "Тормозные диски", 9000, 4),
            Component(7, "Дворники", 3000, 4)
        ]
        self.fabrics = [
            Fabric(1, "АВТОВАЗ"),
            Fabric(2, "УАЗ"),
            Fabric(3, "КАМАЗ"),
            Fabric(4, "УВЗ"),
        ]
        self.fabric_component = [ 
            FabricComponent(1, 1),
            FabricComponent(1, 2),
            FabricComponent(2, 3),
            FabricComponent(3, 4),
            FabricComponent(3, 5),
            FabricComponent(4, 6),
            FabricComponent(4, 7)
        ]

    # Тестирование запроса №1
    def test_request1(self):
        self.assertEqual(
            request1(self.components, self.fabrics), 
            [
            	("Фары", "АВТОВАЗ"),
                ("Тормозные колодки", "АВТОВАЗ"),
                ("Аккумулятор", "КАМАЗ"),
                ("Генератор", "КАМАЗ"),
                ("Заднее крыло", "УАЗ"),
                ("Дворники", "УВЗ"),
                ("Тормозные диски", "УВЗ")
        	]
        )

    # Тестирование запроса №2
    def test_request2(self):
        self.assertEqual(
            request2(self.components, self.fabrics), 
            [
            	("УАЗ", 10000),
                ("УВЗ", 12000),
                ("АВТОВАЗ", 17000),
                ("КАМАЗ", 23000)
            ]
        )

    # Тестирование запроса №3
    def test_request1(self):
        self.assertEqual(
            request3(self.components, self.fabrics, self.fabric_component), 
            {
            	"АВТОВАЗ": ['Тормозные колодки', 'Фары'],
                "УАЗ": ['Заднее крыло'],
                "КАМАЗ": ['Генератор', 'Аккумулятор']
            }
        )


if __name__ == "__main__":
    unittest.main()
