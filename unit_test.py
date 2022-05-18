import re
import unittest

from data_c import main


class Test_Json_CSV(unittest.TestCase):
    def file_format():
        assert re.search("json", main.f_path) == "json"


if __name__ == '__main__':
    unittest.main()
