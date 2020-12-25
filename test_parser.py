import unittest
import parser
import app

class TestParser(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_get_csv_file_content_file_not_found(self):
        response = parser.get_csv_file_content("abc")
        self.assertTrue("ERROR" in response)

    def test_get_csv_file_content(self):
        response = parser.get_csv_file_content("data/Workbook2.csv")
        self.assertTrue("<table" in response)
        self.assertTrue("<tr>" in response)
        self.assertTrue("<td>" in response)


if __name__ == '__main__':
    unittest.main()
