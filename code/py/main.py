from test_script.test_testingP2 import TestTestingP2 

def main():
    p1 = TestTestingP2()
    p1.setup_method("")
    p1.test_testingP2()
    p1.teardown_method("")

if __name__ == "__main__":
    main()

