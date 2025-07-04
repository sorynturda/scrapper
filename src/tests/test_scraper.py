# test_scrapper.py

import unittest
import http
from scrap.scraper import get_info


class TestScrapper(unittest.TestCase):

    def test_inexistent_page(self):
        """
        Url does not exist
        """
        with self.assertRaises(Exception):
            get_info("text inexistent")


    def test_existent_page(self):
        """
        Url exists
        """
        text = get_info("bucuresti")
        self.assertNotEqual(text, "")


if __name__ == "__main__":
    unittest.main()
