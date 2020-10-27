import time
import logging
from traceback import format_exc

from test import Test
from test import bcolors
from drawScreenTest import DrawScreenTest
from vectorTest import VectorTest

class AllTests:
    def __init__(self, tests):
        self.tests = tests
        self.hr = "-------------------"
        self.hr2 = "=============================================="
        self.color = bcolors()

    def run(self):
        result = []

        tm = time.time()
        ok = 0
        count = 0

        for test in self.tests:
            count += 1
            format = "%(asctime)s: %(message)s"
            logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

            logging.info(str(count) + ": Starting test for " + str(test.name) + "...")
            t = time.time()

            if (test.doTest()):
                logging.info(self.hr)
                logging.info("Test done successfully")
                result.append(self.color.okgreen("OK - test for " + str(test.name) + " done successfully"))
                ok += 1
            else:
                logging.info(self.hr)
                logging.info("Test failed")
                result.append(self.color.fail(":( - test for " + str(test.name) + " failed"))

            logging.info(self.hr)
            logging.info("Time: " + str(time.time() - t))
            logging.info(self.hr2)

        logging.info(self.hr2)
        logging.info(self.color.header(str(ok) + " from " + str(len(result)) + " tests done successfully."))
        logging.info(self.hr)
        for i in result:
            logging.info(i)
        logging.info(self.hr)
        logging.info("In time " + str(time.time() - tm) + " s")

if __name__ == "__main__":
    tests1 = []
    tests1.append(DrawScreenTest())
    tests1.append(VectorTest())

    allTests1 = AllTests(tests1)
    allTests1.run()