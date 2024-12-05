import psycopg2

DATABASE_URL = "postgresql://jae_test_user:HtuRJ21AGVyAfz4e2rERt9n8ErU7Wupf@dpg-ct85p923esus73a5lba0-a.frankfurt-postgres.render.com/jae_test"

def list_columns(table_name):
    """
    List all columns in a given table.
    """
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            with connection.cursor() as cursor:
                # Query to fetch column names from information_schema
                cursor.execute("""
                    SELECT column_name, data_type
                    FROM information_schema.columns
                    WHERE table_name = %s;
                """, (table_name,))
                columns = cursor.fetchall()
        return columns
    except psycopg2.Error as e:
        print(f"Error retrieving columns: {e}")
        return None
 
if __name__ == "__main__":
    table_name = "courts"  # Replace with the table you want to inspect
    columns = list_columns(table_name)
    if columns:
        print(f"Columns in '{table_name}':")
        for column in columns:
            print(f" - {column[0]} ({column[1]})")
    else:
        print(f"No columns found for table '{table_name}'.")