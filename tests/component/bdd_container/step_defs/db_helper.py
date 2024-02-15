import psycopg2


class DBHelper:

    @staticmethod
    def get_table_records_count(order_date):
        with psycopg2.connect(database="postgres", user='root', password='berlin', host='db', port='5432') as conn:
            with conn.cursor() as cursor:
                query = f"select count(1) from public.order_data where order_date='{order_date}';"
                cursor.execute(query)
                data = cursor.fetchone()
        return list(data)[0]
