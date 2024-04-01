#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_start(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 20)

    def test_unordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_unordered_larger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([23, 58, 91, 24, 1024, 89, 98,
                                     108, 256, 512]), 1024)

    def test_positives_and_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 108, -256, -512]),
            108)

    def test_positives_and_negatives_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-4232104, 53232772, 3225121, -56562186, -467676870, -41787878916, 64878787843, -97878381,
                    -93232388, 823232552, 352323282, 323232500, 73232924, 2323211, -223232976, 6323232346, -523232405,
                    8323299, -33232432, -22323550, -33232353, 62323944, 9623]), 9323823)

    def test_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-343105619, -843435484449, -6234343553, -33434388955, -343431129454540, -545454817844,
                    -1907189, -8110534, -6601769, -5837524, -4726702,
                    -8433749, -7251403, -5117635, -2979207, -1335257,
                    -2839083, -2586661, -9941097, -3136620]), -71562)

    def test_ints_and_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)

    def test_ints_and_floats_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [22220549.9032254545480645, 308676789.77776767676777, 98676767136.4,
                    393382.5416666667, 15441.826086956522, 2503567,
                    176118.87179487178, 372359.4, 1427676747.61538467676761538,
                    383318.81813232818182, 2923237732.2727272727, 10774980.5276767702702703,
                    99726.62903225806, 4270.788235294118, 490468.4375,
                    54086.6428571423245855, 73068.5, 108526.5081967213, 5767672943.875,
                    128534.875, 61069.433333333334, 37142.71951219512,
                    51481.131147545656098, 571618.5, 35977.166666666664,
                    142333.11764706767676765883, 1767676699123.75]), 67676762503567)

    def test_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [.00123, .457568, .02345, .23423434, .45675674, .678678,
                    .867090, .74653, .5745375]), 0.86709)
                    

    def test_floats_large(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [11.36701449486981136, 12.22932193120425423, 18.269673745943177,
                    1.6021998063297004, 7.040663644666581, 0.318418153098476,
                    4.9723205356754642, 1.0167973840532782,
                    5.17994528432150622, 0.34268959203149724,
                    6.014982685631661026, 0.02477737364433171,
                    5.42770576125452897, 1.7136005979522013,
                    5.877571036363525, 11.6825287480571863, 2.6834294650218338,
                    3.7504024417975861, 2.2762206358275793,
                    8.20607476376994402, 3.9497689034126077,
                    24.1498649449691807]), 49.496355326217376)

    def test_numeric_string(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_string(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lists(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_list(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mixed_list_int_str(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_float(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(9.8)

if __name__ == '__main__':
    unittest.main()