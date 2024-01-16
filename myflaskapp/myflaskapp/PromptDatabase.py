import sqlite3

def create_table_from_schema(db_path, schema):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Extract table name and columns from the JSON schema
    table_name = list(schema['properties'].keys())[0]  # 'Prompt Table'
    columns = schema['properties'][table_name]['items']['properties']

    # Create a SQL command to create the table
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for col_name, col_props in columns.items():
        col_type = "TEXT" if col_props['type'] == "string" else "BLOB"  # Mapping JSON types to SQLite types
        create_table_sql += f"{col_name} {col_type},"
    create_table_sql = create_table_sql.strip(",") + ");"

    # Create the table
    cursor.execute(create_table_sql)
    conn.commit()
    conn.close()


db_path = 'prompt_table.db'
create_table_from_schema(db_path, 'com')
