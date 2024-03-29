import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(0, -5)
        self.assertEqual("0", f.__str__())
        f = Fraction(-0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0,0)
        self.assertEqual("0", f.__str__())
        f = Fraction(2,0)
        self.assertEqual("Infinity with size of 2", f.__str__())
        f = Fraction(-9,0)
        self.assertEqual("Negative infinity with size of 9", f.__str__())
        
    def test_init(self):
        with self.assertRaises(ValueError):
            f = Fraction('hello','fraction')
            f = Fraction([1,2,3],[])
        f = Fraction(1,0)
        self.assertEqual(0,f.numerator)
        self.assertEqual(0,f.denominator)
        self.assertEqual(1,f.inf_size)
        f = Fraction(-2,0)
        self.assertEqual(0,f.numerator)
        self.assertEqual(0,f.denominator)
        self.assertEqual(-2,f.inf_size)
        f = Fraction(0,0)
        self.assertEqual(0,f.numerator)
        self.assertEqual(1,f.denominator)
        self.assertEqual(0,f.inf_size)
        f = Fraction(24,28)
        self.assertEqual(6,f.numerator)
        self.assertEqual(7,f.denominator)
        self.assertEqual(0,f.inf_size)
        f = Fraction(-80,20)
        self.assertEqual(-4,f.numerator)
        self.assertEqual(1,f.denominator)
        self.assertEqual(0,f.inf_size)
        f = Fraction(90,-18)
        self.assertEqual(-5,f.numerator)
        self.assertEqual(1,f.denominator)
        self.assertEqual(0,f.inf_size)
        f = Fraction(-26,-130)
        self.assertEqual(1,f.numerator)
        self.assertEqual(5,f.denominator)
        self.assertEqual(0,f.inf_size)
        f = Fraction(0.5,1)
        self.assertEqual(1,f.numerator)
        self.assertEqual(2,f.denominator)
        self.assertEqual(0,f.inf_size)
        f = Fraction(0.5,0.75)
        self.assertEqual(2,f.numerator)
        self.assertEqual(3,f.denominator)
        self.assertEqual(0,f.inf_size)
        f = Fraction(0,4)
        self.assertEqual(0,f.numerator)
        self.assertEqual(4,f.denominator)
        self.assertEqual(0,f.inf_size)
        f = Fraction(0,-4)
        self.assertEqual(-0,f.numerator)
        self.assertEqual(4,f.denominator)
        self.assertEqual(0,f.inf_size)
        
    def test_add(self):
        with self.assertRaises(ValueError):
            Fraction(2,3) + 'hello'
            Fraction(9,6) + [7.56]
        self.assertEqual(0, Fraction(-2,0)+Fraction(2,0))
        self.assertEqual(Fraction(0,0), Fraction(0,0)+Fraction(0,0))
        self.assertEqual(Fraction(1,2), Fraction(1,2)+Fraction(0,0))
        self.assertEqual(Fraction(9,0), Fraction(9,0)+5)
        self.assertEqual(Fraction(8,0), Fraction(8,0)+Fraction(7,0))
        self.assertEqual(Fraction(8,0), Fraction(8,0)+Fraction(-7,0))
        self.assertEqual(Fraction(-9,0), Fraction(8,0)+Fraction(-9,0))
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(17,60), Fraction(1,12)+Fraction(1,5))
        self.assertEqual(Fraction(1,12), Fraction(1,12)+Fraction(0,5))
        self.assertEqual(Fraction(0,5)+Fraction(1,12), Fraction(1,12)+Fraction(0,5))
        self.assertEqual(Fraction(11,2), Fraction(1,2)+5)
        self.assertEqual(Fraction(-9,2), Fraction(1,2)+(-5))
        self.assertEqual(Fraction(5,4), Fraction(1,2)+0.75)
        self.assertEqual(Fraction(-1,4), Fraction(1,2)+(-0.75))
        self.assertEqual(Fraction(0,4), Fraction(1,2)+Fraction(-1,2))

    def test_sub(self):
        with self.assertRaises(ValueError):
            Fraction(2,3) - 'hello'
            Fraction(9,6) - [7.56]
        self.assertEqual(0, Fraction(-2,0)-Fraction(-2,0))
        self.assertEqual(Fraction(0,0), Fraction(0,0)-Fraction(0,0))
        self.assertEqual(Fraction(1,2), Fraction(1,2)-Fraction(0,0))
        self.assertEqual(Fraction(9,0), Fraction(9,0)-5)
        self.assertEqual(Fraction(8,0), Fraction(8,0)-Fraction(7,0))
        self.assertEqual(Fraction(8,0), Fraction(8,0)-Fraction(-7,0))
        self.assertEqual(Fraction(9,0), Fraction(8,0)-Fraction(-9,0))
        self.assertEqual(Fraction(-7,12), Fraction(1,12)-Fraction(2,3))
        self.assertEqual(Fraction(-7,60), Fraction(1,12)-Fraction(1,5))
        self.assertEqual(Fraction(1,12), Fraction(1,12)-Fraction(0,5))
        self.assertEqual(Fraction(-9,2), Fraction(1,2)-5)
        self.assertEqual(Fraction(11,2), Fraction(1,2)-(-5))
        self.assertEqual(Fraction(-1,4), Fraction(1,2)-0.75)
        self.assertEqual(Fraction(5,4), Fraction(1,2)-(-0.75))
        self.assertEqual(Fraction(1), Fraction(1,2)-Fraction(-1,2))
        
    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        i = Fraction(5,1)
        j = Fraction(90,18)
        k = Fraction(0,0)
        l = Fraction(1,0)
        m = Fraction(2,0)
        self.assertTrue(k == k)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertTrue(f.__eq__(0.5))
        self.assertTrue(i.__eq__(j))
        self.assertTrue(j.__eq__(5))
        with self.assertRaises(ValueError):
            f == 'like'
            g == [1155,[2,6]]

    def test_gt(self):
        with self.assertRaises(ValueError):
            Fraction(2,3) > 'hello'
            Fraction(9,6) > [7.56]
        f = Fraction(5,10)
        g = Fraction(-5,10)
        h = Fraction(0,4)
        i = Fraction(6,0)
        j = Fraction(-5,0)
        k = Fraction(-7,0)
        self.assertTrue(f > g)
        self.assertTrue(f > h)
        self.assertTrue(h > g)
        self.assertFalse(g > h)
        self.assertFalse(g > f)
        self.assertFalse(g > g)
        self.assertFalse(h > h)
        self.assertTrue(i > h)
        self.assertTrue(h > j)
        self.assertTrue(i > j)
        self.assertTrue(i > k)

    def test_mul(self):
        with self.assertRaises(ValueError):
            Fraction(2,3) * 'hello'
            Fraction(9,6) * [7.56]
        self.assertEqual(Fraction(-2,0), Fraction(-2,0)*Fraction(2,0))
        self.assertEqual(Fraction(0,0), Fraction(0,0)*Fraction(0,0))
        self.assertEqual(Fraction(0,0), Fraction(1,2)*Fraction(0,0))
        self.assertEqual(Fraction(9,0), Fraction(9,0)*5)
        self.assertEqual(Fraction(8,0), Fraction(8,0)*Fraction(7,0))
        self.assertEqual(Fraction(-8,0), Fraction(8,0)*Fraction(-7,0))
        self.assertEqual(Fraction(-9,0), Fraction(8,0)+Fraction(-9,0))
        self.assertEqual(Fraction(10,0), Fraction(-10,0)+Fraction(-9,0))
        self.assertEqual(Fraction(1,18), Fraction(1,12)*Fraction(2,3))
        self.assertEqual(Fraction(1,1), Fraction(1,3)*Fraction(3,1))
        self.assertEqual(Fraction(3,20), Fraction(-1,20)*Fraction(3,-1))
        self.assertEqual(Fraction(-50,21), Fraction(-10,3)*Fraction(5,7))
        self.assertEqual(Fraction(0,21), Fraction(-0,3)*Fraction(5,7))
        self.assertEqual(Fraction(-9,40), Fraction(-9,20)*0.5)
        self.assertEqual(Fraction(5,2), Fraction(50,20)*1)
        self.assertEqual(Fraction(0,20), Fraction(0,20)*0)
        self.assertEqual(Fraction(56,123), Fraction(1,123)*56)

    def test_neg(self):
        self.assertEqual(Fraction(2,0), -Fraction(-2,0))
        self.assertEqual(Fraction(-3,0), -Fraction(3,0))
        self.assertEqual(Fraction(0,4), -Fraction(0,4))
        self.assertEqual(Fraction(10,4), -Fraction(-10,4))
        self.assertEqual(Fraction(-8,5), -Fraction(8,5))

if __name__ == '__main__':
     unittest.main(verbosity=2)
