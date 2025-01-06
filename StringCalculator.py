def add(numbers) -> int:

    if not numbers:
       return 0

    delimiter = ','
    if numbers.startswith("//"):
        items = numbers.split('//')
        delimiter=items[1][0]

        numbers= numbers.replace('//'+delimiter,'')

    numbers = numbers.replace('\n',delimiter)
    Parts = numbers.split(delimiter)
    converted=[]
    negative = []
    for i in Parts:
        if i != '':
           value= int(i)
           if value<0:
               negative.append(value)
           converted.append(value)

    if negative:
        print(f"negative numbers not allowed {negative}")
        raise ValueError(f"negative numbers not allowed {negative}")

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

    def test_forwordslash(self):
        result = add("1\n2,3")
        self.assertEqual(result,6)
    def test_delimiter_change(self):
        result = add("//;\n1;2")
        self.assertEqual(result,3)

    def test_negative(self):
        with self.assertRaises(ValueError):
             add("-2,-3,4,5,-3")


if __name__ == "main":
    unittest.main()


