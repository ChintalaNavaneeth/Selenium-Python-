import unittest
from The_Sparks_Foundation import test1, test2, test3, test4, test5


class AppTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("starting Sparks Foundation webitse tests") #runs before all methods starts

    @classmethod
    def tearDownClass(cls):
        print("tested 5pages sucessfully") # runs after all methods ends



    def test_page1(self):
        self.assertTrue(test1.title == "The Sparks Foundation | Home", " title not found ")
        self.assertTrue(test1.logo, "image not found")

    def test_page2(self):
        self.assertTrue(test2.title == "The Sparks Foundation | Home", " title not found ")
        self.assertTrue(test2.img, "image not found")

    def test_page3(self):
        self.assertTrue(test3.title == "The Sparks Foundation | Home", " title not found ")
        self.assertTrue(test3.img, "image not found")

    def test_page4(self):
        self.assertTrue(test4.title == "The Sparks Foundation | Home", " title not found ")
        self.assertTrue(test4.logo, "image not found")

    def test_page5(self):
        self.assertTrue(test5.title == "The Sparks Foundation | Home", " title not found ")
        self.assertTrue(test5.logo, "image not found")

if __name__ == "__main__":
    unittest.main()
