import psycopg2

conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

def read_all_rows():

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table;")
    rows = cursor.fetchall()
    cursor.close()

    return rows

def read_row_by_id(id):

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table WHERE id = %s;", (id,))
    row = cursor.fetchone()
    cursor.close()

    return row

def insert_row(data):

    cursor = conn.cursor()
    cursor.execute("INSERT INTO your_table (column1, column2, ...) VALUES (%s, %s);", (data['column1'], data['column2']))
    conn.commit() 
    cursor.close()

def delete_row(id):

    cursor = conn.cursor()
    cursor.execute("DELETE FROM your_table WHERE id = %s;", (id,))
    conn.commit()  
    cursor.close()

if __name__ == "__main__":

    all_rows = read_all_rows()

    print("All rows:", all_rows)

    row = read_row_by_id(1)

    print("Row with ID 1:", row)

    new_data = {'column1': 'value1', 'column2': 'value2'}
    
    insert_row(new_data)
    delete_row(2)

conn.close()
