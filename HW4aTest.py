import unittest

from main import getUserID
from main import getRepos


class TestInputs(unittest.TestCase):
    
    
    def testSpacesUserID(self): 
        self.assertEqual(getUserID("jgoc eljak"),'Invalid user ID')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()