"""
sql code can be found here:
http://www.newthinktank.com/2014/08/mysql-video-tutorial/
"""

import sqlalchemy

# be sure to turn on msql.server
mysqlengine=sqlalchemy.create_engine("mysql://user:password@localhost/foo")
mysqlengine.execute("CREATE DATABASE IF NOT EXISTS test3;")
# mysqlengine.execute("USE test3")
print mysqlengine
