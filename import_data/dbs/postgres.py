import psycopg2

def get_connection(dbname, user, password, host, port):
    return psycopg2.connect(f"dbname={dbname} user={user} password={password} host={host} port={port}")

def insert_data(conn, table, data):
    try:
      cur = conn.cursor()
      columns = ', '.join(data.keys())
      placeholders = ', '.join(['%s'] * len(data))
      sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
      cur.execute(sql, list(data.values()))
      conn.commit()
      cur.close()
    except Exception as e:
      print(e)
      print(data)
      print("########################################")
      print()
      conn.rollback()
      cur.close()
      # raise e