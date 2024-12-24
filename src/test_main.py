# Unit Tests of the functions in main.py

# Import libraries and files
import unittest
import main
from main import student

# unit test: mean
class TestMean(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(main.my_mean(5, 10), 7.5)
        self.assertEqual(main.my_mean(0, 0), 0)
        self.assertEqual(main.my_mean(-1, 1), 0)

# unit test: divide
class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(main.my_divide(5, 10), 0.5)
        self.assertEqual(main.my_divide(-1, 1), -1)
        self.assertRaises(ValueError, main.my_divide, 10, 0)
        with self.assertRaises(ValueError):
            main.my_divide(0, 0)

# unit test: student
class TestStudent(unittest.TestCase):
    def setUp(self):
        self.s1 = student("student1", 1, "math")
        self.s2 = student("student2", 4, "cs")   
        print("setup")
        return super().setUp()
    
    def tearDown(self):
        print("teardown")
        return super().tearDown()

    def test_age(self):
        self.assertEqual(main.student.age(self.s1.grade), 18)
        self.assertEqual(main.student.age(self.s2.grade), 21)

if __name__ == '__main__':
    unittest.main()