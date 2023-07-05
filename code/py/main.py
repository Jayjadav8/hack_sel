from test_p1 import TestP1

def main():
    print("Entered the main function")
    p1 = TestP1()
    p1.setup_method("")
    p1.test_p1()
    p1.teardown_method("")

if __name__ == "__main__":
    print ("Executed when invoked directly")
    main()

