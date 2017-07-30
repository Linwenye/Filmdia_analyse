import MySQLdb

# attention: this db only connect one time, so it should be close only after it isn't used any more!

# username password
db = MySQLdb.connect("115.159.196.182", "", "", "filmdia")
cursor = db.cursor()
db.set_character_set('utf8')
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')
