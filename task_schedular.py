from apscheduler.schedulers.blocking import BlockingScheduler
from task_profit import ProfitSum

scheduler = BlockingScheduler()


scheduler.add_job(ProfitSum().ana_profit, 'cron', hour=11, minute=26, second=0)


scheduler.start()
