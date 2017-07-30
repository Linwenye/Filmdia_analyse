# -*- coding: UTF-8 -*-
import MySQLdb
from init_cursor import db
from init_cursor import cursor

create_analyse = '''CREATE TABLE TrailerClick(
                imdb_filmID CHAR(9) NOT NULL,
                click_times INT,
                upload_time CHAR(20),
                update_time DATE)DEFAULT CHARSET = utf8'''

create_film = '''CREATE TABLE FilmDB(filmID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
              actors VARCHAR(255),
              country VARCHAR(255),
              directors VARCHAR(255),
              filmType VARCHAR(255),
              filmWatchURL VARCHAR(255),
              imdb_filmID CHAR(9) NOT NULL,
              language VARCHAR(255),
              name VARCHAR(255),
              onTime DATE,
              posterURL VARCHAR(255),
              ratingNum INT,
              score DOUBLE,
              douban_score DOUBLE,
              scriptKeyWords VARCHAR(255),
              summary VARCHAR(1000),
              tagLine VARCHAR(255),
              tags VARCHAR(255),
              cast VARCHAR(1000),
              storyline VARCHAR(1500),
              award VARCHAR(255),
              runtime INT,
              soundmix VARCHAR(255),
              Oscar BOOL,
              budget INT,
              gross INT,
              worldwideGross INT,
              UNIQUE(imdb_filmID) )DEFAULT CHARSET = utf8'''

create_review = 'CREATE TABLE Review(reviewID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,' \
                'helpfulness VARCHAR(255),' \
                'imdb_filmID CHAR(9) NOT NULL,' \
                'score DOUBLE,' \
                'summary VARCHAR(255),' \
                'text VARCHAR(10000),' \
                'time DATE NOT NULL ,' \
                'userName VARCHAR(50) NOT NULL ,' \
                'userCountry VARCHAR(50),' \
                'userInfo_userID INT,' \
                'UNIQUE(userName,imdb_filmID) )DEFAULT CHARSET = utf8'

create_producer = '''CREATE TABLE ProducerDB(producerID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                  films VARCHAR(255),
                  image VARCHAR(255),
                  imdb_producerID CHAR(9) NOT NULL,
                  name VARCHAR(50),
                  producerType VARCHAR(255),
                  UNIQUE (imdb_producerID,producerType) )DEFAULT CHARSET = utf8'''

# 使用execute方法执行SQL语句
cursor.execute(create_analyse)
cursor.execute(create_film)
cursor.execute(create_review)
cursor.execute(create_producer)

# # 使用 fetchone() 方法获取一条数据库。
# data = cursor.fetchone()
#
# print "Database version : %s " % data

# 关闭数据库连接
db.close()
