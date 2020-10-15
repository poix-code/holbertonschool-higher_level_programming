#!/usr/bin/python3
""" Unit testing for Base class"""


import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit testing for Base class.
    """
    def test_zero_args(self):
        """[summary]
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, 2)

    # def test_one_arg(self):
    #     """[summary]
    #     """
    #     base1 = Base(2)
    #     base2 = Base(2)
    #     self.assertEqual(base2.id, base1.id)

    # def test_more_args(self):
    #     """[summary]
    #     """
    #     with self.assertRaises(TypeError):
    #         Base(1, 2, 3)

    # def test_types(self):
    #     """[summary]
    #     """
    #     self.assertEqual([1, 2], Base([1, 2]).id)
    #     self.assertEqual((1, 2), Base((1, 2)).id)
    #     self.assertEqual(True, Base(True).id)
    #     self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)
    #     self.assertEqual({'a': 1, 'b': 2}, Base({'a': 1, 'b': 2}).id)
    #     self.assertEqual('Nan', Base('Nan').id)
    #     self.assertEqual(-10, Base(-10).id)
    #     self.assertEqual(0, Base(0).id)
    #     self.assertEqual('Hi', Base('Hi').id)
    #     self.assertEqual(5.5, Base(5.5).id)
    #     self.assertEqual(complex(1), Base(complex(1)).id)
    #     self.assertEqual(float('inf'), Base(float('inf')).id)


# class Test_Base_to_json_string(unittest.TestCase):
#     """Test to_json_string method
#     """
#     def setUp(self):
#         """[summary]
#         """
#         r1 = Rectangle(2, 3)
#         r2 = Rectangle(4, 5)
#         s1 = Square(5)
#         s2 = Square(10)
#         self.list_sq = [s1.to_dictionary(), s2.to_dictionary()]
#         self.list_rect = [r1.to_dictionary(), r2.to_dictionary()]

#     def test_dict_rectangles(self):
#         """[summary]
#         """
#         self.assertEqual(str, type(Base.to_json_string(self.list_rect)))
#         self.assertTrue(len(Base.to_json_string(self.list_rect)) == 104)
#         self.assertTrue(len(Base.to_json_string([self.list_rect[0]])) == 52)

#     def test_dict_squares(self):
#         """[summary]
#         """
#         self.assertEqual(str, type(Base.to_json_string(self.list_sq)))
#         self.assertFalse(len(Base.to_json_string(self.list_sq)) == 77)
#         self.assertTrue(len(Base.to_json_string([self.list_sq[0]])) == 38)

#     def test_list_Empty(self):
#         """[summary]
#         """
#         self.assertEqual('[]', Base.to_json_string([]))
#         self.assertEqual('[]', Base.to_json_string(None))

#     def test_without_args(self):
#         """[summary]
#         """
#         with self.assertRaises(TypeError):
#             Base.to_json_string()

#     def test_more_than_one_arg(self):
#         """[summary]
#         """
#         with self.assertRaises(TypeError):
#             Base.to_json_string([], 20, 30)


# class Test_Base_to_save_to_file(unittest.TestCase):
#     """Unit testing to_save_to_file clasmethod.
#     """
#     def setUp(self):
#         """[summary]
#         """
#         self.r1 = Rectangle(5, 5, 5, 5, 1)
#         self.r2 = Rectangle(6, 6, 6, 6, 2)
#         self.s1 = Square(4, 4, 4, 3)
#         self.s2 = Square(3, 3, 3, 4)

#     def tearDown(self):
#         """[summary]
#         """
#         if os.path.isfile('Rectangle.json'):
#             os.remove('Rectangle.json')
#         if os.path.isfile('Square.json'):
#             os.remove('Square.json')

#     def test_to_save_one_rect(self):
#         """[summary]
#         """
#         Rectangle.save_to_file([self.r1])
#         with open('Rectangle.json', 'r') as f:
#             self.assertEqual(list, type(json.load(f)))

#     def test_to_save_two_rect(self):
#         """[summary]
#         """
#         Rectangle.save_to_file([self.r1, self.r2])
#         with open('Rectangle.json', 'r') as f:
#             self.assertEqual(list, type(json.load(f)))

#     def test_to_save_one_square(self):
#         """[summary]
#         """
#         Square.save_to_file([self.s1])
#         with open('Square.json', 'r') as f:
#             self.assertEqual(list, type(json.load(f)))

#     def test_to_save_two_square(self):
#         """[summary]
#         """
#         Square.save_to_file([self.s1, self.s2])
#         with open('Square.json', 'r') as f:
#             self.assertEqual(list, type(json.load(f)))

#     def test_to_save_None(self):
#         """[summary]
#         """
#         Square.save_to_file(None)
#         with open('Square.json', 'r') as f:
#             self.assertEqual(0, len(json.load(f)))

#     def test_to_save_empty_list(self):
#         """[summary]
#         """
#         Rectangle.save_to_file([])
#         with open('Rectangle.json', 'r') as f:
#             self.assertEqual(0, len(json.load(f)))

#     def test_to_save_not_args(self):
#         """[summary]
#         """
#         with self.assertRaises(TypeError):
#             Rectangle.save_to_file()

#     def test_to_save_more_args(self):
#         """[summary]
#         """
#         with self.assertRaises(TypeError):
#             Square.save_to_file([], [])


# class Test_Base_from_json_string(unittest.TestCase):
#     """Unit testing for from_json_string method
#     """
#     def setUp(self):
#         """[summary]
#         """
#         self.list_square = [{'id': 89, 'width': 10, 'height': 4},
#                             {'id': 7, 'width': 1, 'height': 7}]
#         self.list_rect = [{'id': 1, 'x': 2, 'size': 10, 'y': 1},
#                           {'id': 2, 'x': 3, 'size': 15, 'y': 2}]

#     def test_output(self):
#         """[summary]
#         """
#         list_input_rect = Rectangle.to_json_string(self.list_rect)
#         list_out_rect = Rectangle.from_json_string(list_input_rect)
#         list_input_sq = Square.to_json_string(self.list_square)
#         list_out_sq = Square.from_json_string(list_input_sq)
#         self.assertEqual(list_out_rect, self.list_rect)
#         self.assertEqual(list_out_sq, self.list_square)

#     def test_None_empty_list(self):
#         """[summary]
#         """
#         self.assertEqual(list(), Base.from_json_string([]))
#         self.assertEqual(list(), Base.from_json_string(None))

#     def test_pass_zero_args(self):
#         """[summary]
#         """
#         with self.assertRaises(TypeError):
#             Base.from_json_string()

#     def test_pass_more_args(self):
#         """[summary]
#         """
#         with self.assertRaises(TypeError):
#             Base.from_json_string([], [])


if __name__ == '__main__':
    unittest.main()
