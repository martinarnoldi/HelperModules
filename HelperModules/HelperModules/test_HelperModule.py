import unittest
import HelperModules
import os

logfilePath = "c:\\temp\\python.log"
maxLogSizeInBytes = 1024

class Test_test_HelperModule(unittest.TestCase):
    def test_Log(self):
        result = os.path.getsize(logfilePath) 
        self.assertLessEqual(result,maxLogSizeInBytes*1024)
        #self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
