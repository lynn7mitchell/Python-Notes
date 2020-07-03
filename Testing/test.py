import unittest

# import file you want to test
import main

class TestMain(unittest.TestCase):
    # test function
    def test_do_stuff(self):
        # test parameter
        test_param = 10
        # variable that grabs the function do_stuff from the file main and gives it the variable test_num
        result = main.do_stuff(test_param)
        # self.assertEqual is seeing if the result is the same as what the solution SHOULD be (15)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        # test parameter
        test_param = 'asdfsadfasdfasd'
        # variable that grabs the function do_stuff from the file main and gives it the variable test_num
        result = main.do_stuff(test_param)
        # self.assertTrue is seeing if the result gives an instance of the value error
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')


if __name__ == '__main__':
    unittest.main()