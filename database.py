import mysql.connector


def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Szkolenie123",
        database="weather_db"
    )

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS weather (
            id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
            odczuwalna FLOAT,
            cisnienie INT,
            wilgotnosc FLOAT,
            temperatura FLOAT,
            opis VARCHAR(255),
            miejsce VARCHAR(255) NOT NULL,
            wiatr FLOAT,
            data DATETIME
        )
    """
    cursor.execute(sql)



def add_record(data):
    print(data)
    try:
        create_table()
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)

        sql = """
        INSERT INTO weather (odczuwalna, cisnienie, wilgotnosc, temperatura, opis, miejsce, wiatr, data)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        values = (
            data["Odczuwalna"],
            data["Ciśnienie"],
            data["Wilgotność"],
            data["Zwykła temperatura"],
            data["Opis pogody"],
            data["Miejsce"],
            data["Prędkość wiatru"],
            data["Data pomiaru"]
        )
        cursor.execute(sql,values)
        connection.commit()
        connection.close()

    except Exception as e:
        print("Błąd połączenia", e)

