import logging
from traceback import format_exc

class Test:
    def __init__(self, name):
        self.name = name
        self.color = bcolors()

    def doTest(self, test):
        try:
            return test.test()
    
        except Exception as e:
            format = "%(asctime)s: %(message)s"
            logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
            print(repr(e))
            print(format_exc())
            return False

    def logError(self, error):
        logging.info("ERROR")
        logging.info("<=========>")
        print(self.color.fail(error))
        logging.info("<=========>")

class bcolors:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKCYAN = '\033[96m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

    def header(self, text):
        return self.HEADER + text + self.ENDC
    def okblue(self, text):
        return self.OKBLUE + text + self.ENDC
    def okcyan(self, text):
        return self.OKCYAN + text + self.ENDC
    def okgreen(self, text):
        return self.OKGREEN + text + self.ENDC
    def warning(self, text):
        return self.WARNING + text + self.ENDC
    def fail(self, text):
        return self.FAIL + text + self.ENDC
    def bold(self, text):
        return self.BOLD + text + self.ENDC
    def underline(self, text):
        return self.UNDERLINE + text + self.ENDC