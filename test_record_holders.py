import record_holder
import sqlite3
from unittest import TestCase

class TestRecordHoldersDB(TestCase):

    test_db = 'test_record_holders.db'

    def setUp(self):

        record_holder.db = self.test_db

        con = sqlite3.connect(self.test_db)
        con.execute('DELETE FROM records')
        con.commit()
        con.close()
    
    def test_add_new_record_holder(self):

        record_holder.add_record_holder('Janne Mustonen', 'Finland', 98)
        record_holder.add_record_holder('Ian Stewart', 'Canada', 94)
        
        expected1 = {'Janne Mustonen', 'Finland', 98}
        expected2 = {'Ian Stewart', 'Canada', 94}
        self.compare_db_to_expected(expected1)
        self.compare_db_to_expected(expected2)

        


        
        
