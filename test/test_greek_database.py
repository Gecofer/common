import unittest
import pyexcel as pe
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from greek_database import process_greek_db

class correspondencesTestCase(unittest.TestCase):

    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_greek_db(self):

        process_greek_db()
        greek_db_to_test = pe.get_sheet(file_name = "data/Greece/processed-db-greece.xlsx")
        new_row_names = greek_db_to_test.row[1]

        # Check first and last name fields
        self.assertEqual(new_row_names[0], "Food name Spanish", "The content of the fields doesn't match")
        self.assertEqual(new_row_names[-1], "Country", "The content of the fields doesn't match")
