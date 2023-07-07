from test_script.test_testingP2 import TestTestingP2 
from test_script.test_p1 import TestP1

def main():
    p1 = TestP1()
    p1.setup_method("")
    p1.test_p1()
    p1.teardown_method("")


    p2 = TestTestingP2()
    p2.setup_method("")
    p2.test_testingP2()
    p2.teardown_method("")

if __name__ == "__main__":
    main()

