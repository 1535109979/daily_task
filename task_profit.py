import json
import time
from datetime import datetime

import pandas as pd
import requests
from sqlalchemy import create_engine, text


class ProfitSum:
    def __init__(self):
        self.engine = create_engine(
            'mysql+pymysql://app:6urA&D$%ji66WuHp@sh-cdb-peeq202o.sql.tencentcdb.com:59964/app?charset=utf8mb4')

        self.url = ('https://oapi.dingtalk.com/robot/send?access_token=71652eb274cd6a8cca66983528c87d0ae85467b3af5920f6c2f357f6127dab55')

    def ana_profit(self):
        a = 10
        while 1:
            try:
                a += 1
                if a > 10:
                    return
                df = self.read_trade_info()
                text = 'sum:'
                text += str(round(df['profits'].sum(), 2)) + '  \n'
                for i in range(len(df)):
                    instrument = df.loc[i].instrument
                    profits = round(df.loc[i].profits, 2)
                    commission = df.loc[i].commissions
                    text += instrument + ' ' + str(profits) + '   \n'
                self.send_msg(text)
                return
            except:
                self.send_msg('read db error')
                time.sleep(5)

    def read_trade_info(self):
        with self.engine.connect() as conn:
            sql = ("select instrument, sum(profits) as profits, sum(commission) as commissions from trade_info "
                   "where account_id='binance_f_226_1234567890' group by instrument;")

            df = pd.read_sql(text(sql), con=conn)
        return df

    def send_msg(self, text: str, isatall=False):
        data = {
            "msgtype": "markdown",
            "markdown": {
                        "title": '## ',
                        "text": datetime.now().strftime('%Y-%m-%d %H:%M:%S  \n') + text
                    },
            "at": {
                "isAtAll": isatall
            }
        }

        requests.post(self.url, headers={'content-type': "application/json"},
                      data=json.dumps(data))


if __name__ == '__main__':
    ProfitSum().ana_profit()

