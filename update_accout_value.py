import sqlite3
import pandas as pd
from sqlalchemy import create_engine, text


def read_db():
    with sqlite3.connect('/Users/edy/byt_pub/a_songbo/vn/data/options_data.db') as conn:
        df = pd.read_sql('SELECT * FROM options_imp', conn)

        # df.to_sql('stocks',conn,if_exists='append', index=False)
        print(df)


def save_mysql():
    pass


def read_mysql():
    engine = create_engine(
        'mysql+pymysql://app:6urA&D$%ji66WuHp@sh-cdb-peeq202o.sql.tencentcdb.com:59964/app?charset=utf8mb4')

    with engine.connect() as conn:
        sql = ("select max(update_time) from songbo_account_value ")
        res = pd.read_sql(text(sql), con=conn)
    return res.loc[0]['max(update_time)']


df = read_mysql()
print(df)
