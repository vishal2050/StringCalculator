def add(numbers) -> int:

    if not numbers:
       return 0

    Parts = numbers.split(',')
    converted=[]
    for i in Parts:
        converted.append(int(i))


    return sum(converted)

import unittest

class TestCalculator(unittest.TestCase):

    def test_Emptystr(self):
        result= add("")
        self.assertEqual(result,0)
    def test_singlenumber(self):
        result = add("1")
        self.assertEqual(result,1)

    def test_twonumbers(self):
        result = add("5,1")
        self.assertEqual(result,6)

if __name__ == "main":
    unittest.main()


