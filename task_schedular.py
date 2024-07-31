from apscheduler.schedulers.blocking import BlockingScheduler
from task_profit import ProfitSum

scheduler = BlockingScheduler()


scheduler.add_job(ProfitSum().ana_profit, 'cron', hour=9, minute=0, second=0)


scheduler.start()
