from database.connection import get_connection
class BookingDAO:
    def save(self, customer_mobile_number):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO customer(mobile_number)VALUES (?)""", (customer_mobile_number,))
        connection.commit()
        connection.close()
        return True

    def find_all(self):
        connection = get_connection()
        cursor= connection.cursor()
        cursor.execute("""select * from booking""")
        result = cursor.fetchall()
        return result

    def find_customer(self,customer_mobile_num):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""select customer_id from customer where mobile_number = ?""",(customer_mobile_num,))
        result =cursor.fetchone()
        return result
