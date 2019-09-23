import sqlite3

con = sqlite3.connect('chainsaw_juggling_db.sqlite')

db = 'chainsaw_juggling_db.sqlite'

con.execute('CREATE TABLE IF NOT EXISTS records (name TEXT, country TEXT, number_catches INTEGER)')

con.commit()
con.close()

def add_record_holder(name, country, number_catches):

    insert_data = 'INSERT INTO records (name, country, number_catches) VALUES (?, ?, ?)'

    with sqlite3.connect(db) as con:
        con.execute(insert_data, (name, country, number_catches))
    
    con.close()

def search_record_holder(name):

    search_data = 'SELECT * FROM records WHERE name = ?'
    
    with sqlite3.connect(db) as con:
        con.execute(search_data, (name, ))
    
    record_rows = con.fetchall()

    for record in record_rows:
        print('Name: ', record[0], ' | ', 'Country: ', record[1], ' | ', 'Number Catches: ', record[2])

    con.close()

def update_record_holder(number_catches, name):
    
    update_data = 'UPDATE records SET number_catches = ? WHERE name = ?'

    with sqlite3.connect(db) as con:
        updated = con.execute(update_data, (number_catches, name))
        row_updated = updated.rowcount
    con.close()

    if row_updated == 0:
        raise RecordError('Record cannot be found')
    
def delete_record_holder(name):

    delete_data = 'DELETE FROM records WHERE name = ?'

    with sqlite3.connect(db) as con:
        deleted = con.execute(delete_data, (name, ))
        deleted_count = deleted.rowcount
    con.close()

    if deleted_count == 0:
        raise RecordError('Record cannot be found')

def main():

    running = True

    while running:
        user_choices = menu()

        if user_choices == 1:
            name = input('Enter the record holder name: ')
            country = input('Enter the country where the record holder from: ')
            number_catches = int(input('Enter the number of catches: '))
            add_record_holder(name, country, number_catches)
        elif user_choices == 2:
            search_name = input('Enter the name that you would like to find: ')
            search_record_holder(search_name)
        elif user_choices == 3:
            update_name = input('Enter the name of the record holder that need to be updated: ')
            number_catches = int(input('Enter the new number of catches: '))
            update_record_holder(number_catches, update_name)
        elif user_choices == 4:
            delete_name = input("Enter the name of the person in the record that you want to delete: ")
            delete_record_holder(delete_name)
        elif user_choices == 5:
            running = False
            print('Thank you and goodbye!')


    return user_choices

def menu():
    print('-Chainsaw Juggling Record Holders July 2018- \n')
    print('1. Add Record Holder')
    print('2. Search record holder name')
    print('3. Update the number of catches')
    print('4. Delete record by name')
    print('5. Quit')
    user_input = int(input('Enter choice: '))

    if not 1 <= user_input < 6:
        print('Please enter a number between 1-5.')
    else:
        return user_input    

    return user_input

class RecordError(Exception):
    pass

if __name__ == '__main__':
    main()


    




    
    
    




