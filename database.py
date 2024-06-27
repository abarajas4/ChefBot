import pandas as pd
import sqlalchemy as db
## SQL 
engine = db.create_engine('sqlite:///data_base_name.db')
dataframe_name.to_sql('table_name', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))
