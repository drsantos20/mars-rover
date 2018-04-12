import rover
import unittest
r = rover.rover()

class TestSequenceFunctions(unittest.TestCase):


    def test_x_coordinate(self):
        global r
        r.set_data([5, 5], 1, 2, 'N', 'LMLMLMLMM')
        r.coordinates_follow()
        results = r.get_result()
        self.assertEqual(results[0], 1)
    def test_y_coordinate(self):
        global r
        r.set_data([5, 5], 3, 3, 'E', 'MMRMMRMRRM')
        r.coordinates_follow()
        results = r.get_result()
        self.assertEqual(results[1], 1)
    def test_direction(self):
        global r
        r.set_data([6, 6], 2, 4, 'S', 'MRMLMMRLMRM')
        r.coordinates_follow()
        results = r.get_result()
        self.assertEqual(results[2], 'W')

        
if __name__ == '__main__':
    unittest.main()