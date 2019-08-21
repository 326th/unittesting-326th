import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):

    def test_unique_sigleton_list(self):
        self.assertEqual([5],unique([5]))
        self.assertEqual([[1,2,3]],unique([[1,2,3]]))
        self.assertEqual(['a'],unique(['a']))
        self.assertEqual([4.5062],unique([4.5062]))
    def test_unique_empty_list(self):
        self.assertEqual([],unique([]))
    def test_unique_unexpected_value(self):
        with self.assertRaises(ValueError):
            unique('this is not a list')
            unique(3.141592653)
            unique({'a':'apple','b':'bird'})
    def test_unique_normal_list(self):
        self.assertEqual([4,6,5,7],unique([4,4,6,4,5,6,7,5,6,5]))
        self.assertEqual(['cat','dog','fish'],unique(['cat','dog','dog','cat','cat','fish']))       
    def test_unique_mixed_list(self):
        self.assertEqual([5,2,'Digger',4,'Farmer',6,7],unique([5,2,'Digger',4,'Farmer',5,6,7,'Digger','Digger',2,5]))
        self.assertEqual([[1,2,3],[3,2,1],1,8,[5],6,7,'test',4,[4,5,67]],unique([[1,2,3],[3,2,1],1,8,[5],[3,2,1],6,7,8,'test',1,4,[4,5,67],[3,2,1]]))
    def test_unique_large_list(self):
        unique_input = []
        for i in range(1,22):
            for j in range(1,i):
                unique_input.append(j) #list is[1,1,2,1,2,3,1,2,3,4,...,20]
        result = []
        for i in range(1,21):
            result.append(i) #list is [1,2,3,...,20]
        self.assertEqual(result,unique(unique_input))

if __name__ == '__main__':
    unittest.main('listutil_test')
            
