# All codes related to connection
from sqlalchemy import create_engine
from urllib.parse import quote_plus

class  CreateMySQLInstance:

    def __init__(self):
       # dialect+driver://username:password@host:port/database
       password=quote_plus("Shiv28@joi")
       username="root"
       db_name="python_sql"
       server_address="localhost:3306"
       self.engine=create_engine(f"mysql+pymysql://{username}:{password}@{server_address}/{db_name}")


    def get_engine(self):
        return self.engine
