
import pytest
import unitest

class TestStringMethods(unittest.TestCase):

def test_reversestr(self):
    self.assert StringUtils.reversestr("nokia") == "aikok"
    self.assert StringUtils.reversestr("task") == "ksat"
    

def test_palindrome(self):
    self.assert StringUtils.palindrome("madam") is True
   self.assert StringUtils.palindrome("nokia") is False
     

if __name__ == "__main__":
    pytest.main()




A testcase is created by subclassing unittest.TestCase. 
Two tests are defined with methods whose names start with the letters test.  
The crux of each test is a call to assert() to check for an expected result 
 