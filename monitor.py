import time
import csv
from datetime import datetime
class Monitor:
    MAX_TIME=45*60
    def __init__(self,log_file="data/usagelog.csv"):
        self.log_file=log_file
    def log_event(self,tap):
        with open(self.log_file,mode='a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime("%Y/%m/%d, %H:%M:%S"),tap.tap_id,tap.state,tap.flow_rate])
    def check_unattended(self,tap):
        if tap.state=="ON":
            if time.time()-tap.start_time>self.MAX_TIME:
                return True
        return False
