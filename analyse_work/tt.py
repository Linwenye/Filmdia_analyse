from db_helper.init_cursor import db
from db_helper.init_cursor import cursor


def get_exist_list():
    exist_tup = cursor.fetchall()
    exists = list()
    for a_item in exist_tup:
        exists.append(a_item[0])
    return exists


cursor.execute('SELECT imdb_filmID FROM UpdateFilm ')
filmids = get_exist_list()
cursor.execute('SELECT imdb_filmID FROM TrailerClick')
all_ids = get_exist_list()
for a_id in all_ids:
    if a_id not in filmids:
        cursor.execute('DELETE FROM TrailerClick WHERE imdb_filmID=%s', (a_id,))
db.commit()

