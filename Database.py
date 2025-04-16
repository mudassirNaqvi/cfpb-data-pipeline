def data_sql():
    import json
    import mysql.connector

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="Complain" 
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data JSON  -- This column stores the JSON data
        )
    """)

    conn.commit()

    with open("/home/mudassir/airflow/dags/data.json", 'r') as file:
        data = json.load(file)  

    sql = "INSERT INTO complaints (data) VALUES (%s)"

    for complaint in data:
        cursor.execute(sql, (json.dumps(complaint),))

    conn.commit()
    cursor.close()
    conn.close()

    print("json data successfully dumped into Mysql")
