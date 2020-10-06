from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey




class Database:
    DBases= {
        'sqlite': 'sqlite:///{DB}'
    }

    def __init__(self, dbtype, username='', password='', dbname=''):
        db_engine = None
        dbtype = dbtype.lower()
        if dbtype in self.DBases.keys():
            engine_url = self.DBases[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("Name of Database not Valid")

    def _execute_query(self, query=''):
        if query == '' : return
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def _get_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row) 
                result.close()

    def ensure_column_exists(self, table='', column='', type=''):
        #cur=self.db_engine.cursor()
        for row in self.db_engine.execute('PRAGMA table_info({})'.format(table)):
            if row[1] == column:
                print('column {} already exists in {}'.format(column, table))
                break
        else:
            print('add column {} to {}'.format(column, table))
            self.db_engine.execute('ALTER TABLE {} ADD COLUMN {} {}'.format(table, column, type))
        #self._execute_query(query='ALTER TABLE {} ADD COLUMN {} {};'.format(table,column,type))
        self._get_data(table)

    def set_cell_value(self,table='', column='', column_value='', id='', id_value=''):
        self._execute_query(query='UPDATE {} set {}={} WHERE {}={}'.format(table, column, column_value, id, id_value))
        self._get_data(table)