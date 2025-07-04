# test_encryption.py

import unittest
import os
from scrap.encryption import encrypt_data, decrypt_data

class TestEncryption(unittest.TestCase):



    def test_encrypt(self):
        """
        test if the content is encrypted
        """

        text = "some text"
        encrypt_data(text, "test_file")
        with open("wiki/" + "test_file.dat",'r') as f:
            content = f.read()
        self.assertNotEqual(text, content)
        os.remove("wiki/test_file.dat")
    
    def test_saved_file(self):
        text = "asdjkas"
        file_name = "test_file"
        encrypt_data(text, file_name)
        self.assertTrue(os.path.exists("wiki/" + file_name + '.dat'), True)
        os.remove("wiki/" + file_name + '.dat')

    def test_no_data_loss(self):
        text = "asdjkas"
        file_name = "test_file"
        encrypt_data(text, file_name)
        self.assertEqual(text, decrypt_data(file_name))
        os.remove("wiki/" + file_name + '.dat')

if __name__ == "__main__":
    unittest.main()
