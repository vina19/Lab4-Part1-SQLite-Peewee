import sqlite3

conn = sqlite3.connect('record_holder_db.sqlite')

db = 'record_holder_db.sqlite'

class chainsaw_juggling_record:

    def create_table_sql(self):

        create_table = 'CREATE TABLE IF NOT EXISTS records (name TEXT, country TEXT, number_catches INTEGER)'

        con = sqlite3.connect(db)

        with con:
            con.execute(create_table)
        
        con.close()
    
    def add_record_holder(self, record):

        insert_data = 'INSERT INTO records (name, country, number_catches) VALUES (?, ?, ?)'

        with sqlite3.connect(db) as con:
            con.execute(insert_data, (record.name, record.country, record.number_catches))

        con.close()
    
    def search_record_holder(self, name):

        search_data = 'SELECT * FROM records WHERE name = ?'

        with sqlite3.connect(db) as con:
            con.execute(search_data, (name, ))
        
        con.close()
    




