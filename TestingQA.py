# Implementasi white-box testing dalam Python menggunakan library unittest. 

import unittest

def total(angka):
    total = 0
    for num in angka:
        total += num
    return total

class TestTotal(unittest.TestCase):
    def test_total_positif(self):
        angka = [1, 2, 3, 4, 5]
        self.assertEqual(total(angka), 15)
    
    def test_total_negatif(self):
        angka = [-1, -2, -3, -4, -5]
        self.assertEqual(total(angka), -15)

    def test_total_campuran(self):
        angka = [1, -2, 3, -4, 5]
        self.assertEqual(total(angka), 3)

    def test_total_kosong(self):
        angka = []
        self.assertEqual(total(angka), 0)

if __name__ == '__main__':
    unittest.main()