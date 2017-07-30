from crawler_util import page_read
from db_helper.init_cursor import cursor
from db_helper.init_cursor import db
import re


def get_exist_list():
    exist_tup = cursor.fetchall()
    exists = list()
    for a_item in exist_tup:
        exists.append(a_item[0])
    return exists


def get_num(s):
    if s.find('(') >= 0:
        s = s[:s.find('(')]
    res = ''
    pattern = '[0-9]+'
    numlist = re.findall(pattern, s)
    for item in numlist:
        res += item
    if res != '':
        return int(res)
    else:
        return 0


def get_weekgross(s):
    for item in s:
        if item.h4:
            if item.h4.string:
                if item.h4.string.startswith('Opening Weekend'):
                    return get_num(item.get_text())


cursor.execute(
    'SELECT FilmDB.imdb_filmID '
    'FROM FilmDB,TrailerClick '
    'WHERE FilmDB.imdb_filmID=TrailerClick.imdb_filmID '
    'AND (country=\'USA\'OR country=\'UK\') AND gross>1000000 and openweek_gross is null')

filmids = get_exist_list()
print filmids
for filmid in filmids:
    soup = page_read.page_read_nolog('http://www.imdb.com/title/' + filmid + '/')
    if soup.select('.txt-block'):
        weekgross = get_weekgross(soup.select('.txt-block'))
        if weekgross and weekgross != 0:
            cursor.execute(
                '''UPDATE TrailerClick SET openweek_gross=%s WHERE imdb_filmID=%s''',
                (weekgross, filmid))
            db.commit()
