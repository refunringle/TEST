import psycopg2

def get_connection(dbname="blog"):
    return psycopg2.connect(f"dbname={dbname}")


# def add_artist(artist_name):
#     conn = get_connection()
#     with conn.cursor() as curs:
#         curs.execute("INSERT INTO post(name) VALUES(%s)", (artist_name,))
#         curs.execute("SELECT id FROM artists ORDER BY id DESC")
#         id = curs.fetchone()[0]
#     conn.commit()
#     conn.close()
    # return id

def add_user(id,name,email,password):
    conn = get_connection()
    with conn.cursor() as curs:
        curs.execute("INSERT INTO songs(name, artist_id, lyrics) VALUES(%s,%s, %s)",
         (song_name, artist_id, lyrics))
    conn.commit()
    conn.close()

def add_post(id,user_name,title,category,summary,content,publish_time,tag):
    conn = get_connection()
    with conn.cursor() as curs:
        curs.execute("INSERT INTO songs(name, artist_id, lyrics) VALUES(%s,%s, %s)",
         (song_name, artist_id, lyrics))
    conn.commit()
    conn.close()

def add_post_comment(id,post_id,guest_name,publish_time,content):
    conn = get_connection()
    with conn.cursor() as curs:
        curs.execute("INSERT INTO songs(name, artist_id, lyrics) VALUES(%s,%s, %s)",
         (song_name, artist_id, lyrics))
    conn.commit()
    conn.close()    


