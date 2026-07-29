from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
# DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/db"
DATABASE_URL = mysql+pymysql://avnadmin:AVNS_3rQc2Bi7Er4norqWL9-@mysqldb-ketangoud938-6f1e.j.aivencloud.com:15620/defaultdb

engine = create_engine(DATABASE_URL,connect_args={"ssl":{}})

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
