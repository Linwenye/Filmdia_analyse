from db_helper.init_cursor import cursor
from db_helper.init_cursor import db


def get_exist_list():
    exist_tup = cursor.fetchall()
    exists = list()
    for a_item in exist_tup:
        exists.append(a_item[0])
    return exists


cursor.execute('SELECT tags FROM FilmDB')
res = dict()
tags = get_exist_list()
for dd in tags:
    for tag in dd.split('/'):
        if tag!='':
            res[tag] = res.get(tag, 0) + 1
print res
