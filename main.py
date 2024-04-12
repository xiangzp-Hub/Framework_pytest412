import os
import pytest

if __name__ == '__main__':
    pytest.main()
    report_temp = r'testReport\report\temps'
    report_dir = r'testReport\report\allure'
    # os.system('allure generate' + report_temp + '-o' + report_dir + "--clean")
    os.system("allure generate ./testReport/report/temps -o ./testReport/report/allures --clean")
