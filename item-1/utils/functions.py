def create_user(conn, cur, user):
    """
    Inserts the user into the database
    
    :param conn: the connection to the database
    :param cur: the cursor object
    :param user: a tuple of the form (username, fullname, password, isAdmin)
    :return: The user id
    """
    sql = '''INSERT INTO Users (Username,Fullname,Password,IsAdmin) VALUES (?,?,?,?)'''

    cur.execute(sql, user)
    
    conn.commit()

    return cur.lastrowid