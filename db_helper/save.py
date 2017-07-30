import logging
import traceback
import MySQLdb
import datetime
from init_cursor import db
from init_cursor import cursor


def my_map(my_dict, my_key):
    if my_dict.has_key(my_key):
        return my_dict[my_key]
    else:
        return None


def my_map_double(my_dict, my_key):
    if my_dict.has_key(my_key):
        return my_dict[my_key]
    else:
        return 0


def list_to_string(my_list):
    res = ''
    if not my_list:
        return res
    for item in my_list:
        res = res + item + '/'
    return res


def save_click(imdb_filmID, click_times, upload_time):
    click_sql = '''REPLACE INTO filmdia.TrailerClick
    (imdb_filmID,click_times,upload_time,update_time) VALUES (%s,%s,%s,%s)'''
    click_data = (imdb_filmID, click_times, upload_time, datetime.date.today())
    try:
        cursor.execute(click_sql, click_data)
        db.commit()
    except Exception as e:
        db.rollback()
        print 'insert wrong'
        logging.error(traceback.format_exc())
