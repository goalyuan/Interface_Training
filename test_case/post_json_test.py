import unittest
from public import base

testcasefile = 'post_json_test_data.xlsx'
AllData = base.get_data(testcasefile, 'AllData')
TestData = base.get_data(testcasefile, 'TestData')
EndPoint = AllData[1][1]
RequestMethod = AllData[1][2]
Sn = TestData[1][0]
RequestData = TestData[1][1]
Expectedresult = TestData[1][1]


class PostJsonTest(unittest.TestCase):
    def setUp(self):
        self.url = base.get_url(EndPoint)

    def test_post_json(self):
        DataALL = eval(RequestData)
        Method = RequestMethod
        resp = base.get_response(self.url, Method, **DataALL)
        name = resp['data']
        self.assertIsInstance(name, str)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
