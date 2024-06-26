import psycopg2

def get_connection(dbname, user, password, host, port):
    return psycopg2.connect(f"dbname={dbname} user={user} password={password} host={host} port={port}")

def insert_data(table, data):
    try:
      conn = get_connection('postgres', 'postgres', 'example', 'localhost', '5432')
      cur = conn.cursor()
      columns = ', '.join(data.keys())
      placeholders = ', '.join(['%s'] * len(data))
      sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
      cur.execute(sql, list(data.values()))
      conn.commit()
      cur.close()
      return "Data inserted successfully", 200
    except Exception as e:
      print(e)
      print(data)
      print("########################################")
      print()
      conn.rollback()
      cur.close()
      return e.args, 500
      

def get_data(table, id=None):
    conn = get_connection('postgres', 'postgres', 'example', 'localhost', '5432')
    cur = conn.cursor()
    if id:
        cur.execute(f"SELECT * FROM {table} WHERE storeid = %s", (id,))
    else:
        cur.execute(f"SELECT * FROM {table} ORDER BY storeid ASC")
    columns = [desc[0] for desc in cur.description]
    data = cur.fetchall()
    data = [dict(zip(columns, row)) for row in data]
    cur.close()
    conn.close()

    return data, 200

def update_data(table, id, data):
    conn = get_connection('postgres', 'postgres', 'example', 'localhost', '5432')
    cur = conn.cursor()
    info = ', '.join([f"{key} = %s" for key in data.keys()])
    sql = f"UPDATE {table} SET {info} WHERE storeid = %s"
    print(sql)
    cur.execute(sql, list(data.values()) + [id])
    conn.commit()
    cur.close()
    conn.close()
    status = "Data updated successfully" if cur.rowcount else "Data not found"
    code = 200 if cur.rowcount else 404
    new_data, _ =  get_data(table, id)
    return {"msg": status, "data": new_data}, code

def delete_data(table, id):
    conn = get_connection('postgres', 'postgres', 'example', 'localhost', '5432')
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table} WHERE storeid = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    status = "Data deleted successfully" if cur.rowcount else "Data not found"
    return status, 200
    