import sqlite3

# Create connection to database
con = sqlite3.connect('chainsaw_juggling_db.sqlite')

# Create variable for database
db = 'chainsaw_juggling_db.sqlite'

# Create a table name records if it doesn't exist
con.execute('CREATE TABLE IF NOT EXISTS records (name TEXT, country TEXT, number_catches INTEGER)')

# Add data for testing
con.execute('INSERT INTO records VALUES ("Janne Mustonen", "Finland", 98)')
con.execute('INSERT INTO records VALUES ("Ian Stewart", "Canada", 94)')
con.execute('INSERT INTO records VALUES ("Aaron Gregg", "Canada", 88)')
con.execute('INSERT INTO records VALUES ("Chad Tayor", "USA", 78)')

# Commit and close the connection
con.commit()
con.close()

# Adding record to the database
def add_record_holder(name, country, number_catches):

    insert_data = 'INSERT INTO records (name, country, number_catches) VALUES (?, ?, ?)'

    with sqlite3.connect(db) as con:
        con.execute(insert_data, (name, country, number_catches))
    con.commit()
    
# Search record holder by their name from database
def search_record_holder(name):

    search_data = 'SELECT * FROM records WHERE name = ?'
    
    with sqlite3.connect(db) as con:
        con.execute(search_data, (name, ))
    
    # http://www.mysqltutorial.org/python-mysql-query/
    record_rows = con.fetchall()

    # Display record from database
    for record in record_rows:
        print('Name: ', record[0], ' | ', 'Country: ', record[1], ' | ', 'Number Catches: ', record[2])

    con.close()

# Update the number of catches by their name in database
def update_record_holder(number_catches, name):
    
    update_data = 'UPDATE records SET number_catches = ? WHERE name = ?'

    with sqlite3.connect(db) as con:
        updated = con.execute(update_data, (number_catches, name))
        row_updated = updated.rowcount # Show how many rows affected
    con.commit()

    # Raise RecordError if there is no record
    if row_updated == 0:
        raise RecordError('Record cannot be found')

    # If the number of cathces input is not number raise RecordError
    if not isinstance(number_catches, (int)) or number_catches < 0:
        raise RecordError('Please enter a valid number and positive number.')

# Delete record in database by record holder's name
def delete_record_holder(name):

    delete_data = 'DELETE FROM records WHERE name = ?'

    with sqlite3.connect(db) as con:
        deleted = con.execute(delete_data, (name, ))
        deleted_count = deleted.rowcount # Show how many row affected
    con.close()
    
    # Raise RecordError if there is no record
    if deleted_count == 0:
        raise RecordError('Record cannot be found')

# Display of the menu options for the user
def menu_options():
    print('-Chainsaw Juggling Record Holders July 2018- \n')
    print('1. Add Record Holder')
    print('2. Search record holder name')
    print('3. Update the number of catches')
    print('4. Delete record by name')
    print('5. Quit')
    user_input = int(input('Enter choice: '))

    # if the user enter number outside 1-6 print error message
    if not 1 <= user_input < 6:
        print('Error: please enter a number between 1-5.')
    else:
        return user_input    

# Main method
def main():

    running = True
    while running:
        # Display the menu
        user_choices = menu_options()

        # Get the user input, depend on the number option they choose
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

# Record Errors
class RecordError(Exception):
    pass

if __name__ == '__main__':
    main()