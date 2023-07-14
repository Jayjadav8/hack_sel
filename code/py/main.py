from test_script.test_unregistered_id import TestTestingP2 
from test_script.test_p1 import TestP1
from test_script.test_page2Loginpage import TestPage2Loginpage
from test_script.test_page3browseSearchpagewithoutlogin import TestPage3browseSearchpagewithoutlogin


def main():
    p1 = TestP1()
    p1.setup_method("")
    p1.test_p1()
    p1.teardown_method("")


    p2 = TestTestingP2()
    p2.setup_method("")
    p2.test_testingP2()
    p2.teardown_method("")


    p3 = TestPage2Loginpage()
    p3.setup_method("")
    p3.test_page2Loginpage()
    p3.teardown_method("")

    p4 = TestPage3browseSearchpagewithoutlogin()
    p4.setup_method("")
    p4.test_page3browseSearchpagewithoutlogin()
    p4.teardown_method("")




if __name__ == "__main__":
    main()

