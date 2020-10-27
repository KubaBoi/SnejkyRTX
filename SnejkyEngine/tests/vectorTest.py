from test import Test
import sys
import os
import math

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from vector import Vector

class VectorTest(Test):
    def __init__(self):
        self.name = "Vector calculations"
        Test.__init__(self, self.name)

    def doTest(self):
        return Test.doTest(self, self)

    def test(self):
        ok = True
        vector = Vector(5, 4, 6)

        result = vector.selfLength()
        if (result != math.sqrt(77)):
            ok = False
            Test.logError(self, "       selfLength() test error:" +
            "\n       Actual: " + str(result) + 
            "\n       Expected: " + str(math.sqrt(77)))

        return ok