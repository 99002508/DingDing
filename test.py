import unittest
from server import *
from client import *

class ServerTest(unittest.TestCase):
    def my_test(self):
        self.assertEqual(server_program(),"done")		
class ClientTest(unittest.TestCase):
    def my_test1(self):
        self.assertEqual(client_program(),"done")
if __name__ == '__main__':
    unittest.main()
