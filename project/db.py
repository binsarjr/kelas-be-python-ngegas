import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="kelaspython",
    user="postgres",
    password="postgres",
)


# Set the default schema
default_schema = "project"
with conn.cursor() as cursor:
    cursor.execute(f"SET search_path TO {default_schema}")

print("DONE setting schema name")
