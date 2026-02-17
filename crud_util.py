# All functions related to create,read,update,delete

import sql_util as sql
from  sqlalchemy import text 
import pandas  as pd

# create table

def create_table():
    # sql_instance = sql.CreateMySQLInstance()
    #engine = sql_instance.get_engine()
    engine = sql.CreateMySQLInstance().get_engine()
    sql_query = """create table if not exists employee(
        emp_id int primary key auto_increment,
        name varchar(50) not null,
        email varchar(55) not null unique,
        gender varchar(10) not null
    )"""

    with  engine.connect() as connection:
        connection.execute(text(sql_query))
        print("Table created successfully")

   # insert
def insert_employee(n,g,em):
    engine=sql.CreateMySQLInstance().get_engine()
    insert_query="""insert into employee(name,email,gender)
                     values(:emp_name, :emp_email, :emp_gender)"""
    

    try:
            with  engine.connect() as connection:
                result=connection.execute(text(insert_query),{"emp_name":n,"emp_email":em,"emp_gender":g})
                connection.commit()
                print(f"Employee  saved successfully Row affected ={result.rowcount}")

    except Exception as e:
         print(e)


def find_all_employee():
        engine =sql.CreateMySQLInstance().get_engine()
        select_sql ="select * from employee"

        try:
             df=pd.read_sql(select_sql,engine)
             print(df)
        except  Exception as e:
             print(e)


def find_employee_by_id(id):
      engine =sql.CreateMySQLInstance().get_engine()
      select_sql =f"select * from employee where emp_id={id}"

      try:
             df=pd.read_sql(select_sql,engine)
             if not df.empty:
              print(df)
             else:
                  print(f"Employee with emp_id= {id} not found")
                  return not df.empty
      except Exception as e:
           print(e)

def  delete_emp_by_id(id):
     engine=sql.CreateMySQLInstance().get_engine()

     if find_employee_by_id(id):
          delete_query="delete from employee where emp_id= :e_id"

          try:
               with engine.connect() as connection:
                    result=connection.execute(text(delete_query),{"e_id":id})
                    connection.commit()
                    print(f"Employee with emp id:{id} deleted successfully.Rows affected ={result.rowcount}")
          except Exception as e:
               print(e)

    

