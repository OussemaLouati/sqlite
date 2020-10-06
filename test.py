from connect import Database

dbms = Database("sqlite", dbname='testdb.sqlite')

#dbms._get_data('USERS1')
#dbms._get_data('USERS2')



#dbms.ensure_column_exists("USERS2", "session_id", "INTEGER")
#dbms.ensure_column_exists("USERS1", "session_id", "INTEGER")


#dbms.set_cell_value("USERS1", "session_id", 13, "id", 1)
#dbms.set_cell_value("USERS2", "session_id", 13, "id", 5)