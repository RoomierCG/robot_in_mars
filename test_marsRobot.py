import unittest
from unittest import mock
from mars_robot import * 

class TestMarsRobotTerrainGeneration(unittest.TestCase):

    def setUp(self):
        print("Setting Up")

    @mock.patch('mars_robot.input', create=True)
    def testTerrainLength(self, mocked_input):
        mocked_input.side_effect = ['11x10']
        result = generate_terrain()
        self.assertGreater(len(result), 0)

    @mock.patch('mars_robot.input', create=True)
    def testTerrainNumberPositives(self, mocked_input):
        mocked_input.side_effect = ['11x10'] #-11x-9
        result = generate_terrain()

        if int(result[0]) < 0:
            self.assertGreater(int(result[0]), 0)
        elif int(result[1]) < 0:
            self.assertGreater(int(result[1]), 0)

if __name__ == "__main__":
    unittest.main()