from test_script.test_p1 import TestP1

def main():
    p1 = TestP1()
    p1.setup_method("")
    p1.test_p1()
    p1.teardown_method("")

if __name__ == "__main__":
    main()

