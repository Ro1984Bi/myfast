from sqlalchemy import create_engine, MetaData, engine

engine = create_engine("mysql+pymysql://root:@localhost:3306/storedb")

meta = MetaData()

conn =  engine.connect()