import unittest
import os
import sys

# Importing Modules From Different Directory: https://csatlas.com/python-import-file-module/ 
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'topic_0' )
sys.path.append( mymodule_dir )
import something

something.hello()

# Ref: https://docs.python.org/3/library/unittest.html
class TestSort(unittest.TestCase):
    def test(self):
        result = something.hello()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()