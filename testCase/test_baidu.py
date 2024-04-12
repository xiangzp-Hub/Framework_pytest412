import pytest
import requests


class TestApi:

    def test01_baidu(self):
        url = 'https://www.baidu.com/'
        res = requests.get(url)
        print(res.status_code)

    def test02_baidu(self):
        url = 'https://www.baidu.com/'
        res = requests.get(url)
        print(res.status_code)

    def test03_baidu(self):
        url = 'https://www.baidu.com/'
        res = requests.get(url)
        print(res.status_code)

    def test04_baidu(self):
        url = 'https://www.baidu.com2222/'
        res = requests.get(url)
        print(res.status_code)


if __name__ == '__main__':
    pytest.main(["-vs"])
