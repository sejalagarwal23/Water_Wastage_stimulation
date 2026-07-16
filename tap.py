import time
class Tap:
    def __init__(self,tap_id):
        self.tap_id=tap_id
        self.state="off"
        self.flow_rate='0'
        self.start_time=None
    def turn_on(self,flow_rate):
        self.state="ON"
        self.start_time=time.time()
        self.flow_rate=flow_rate
    def turn_off(self):
        self.state="off"
        self.flow_rate=0
        self.start_time=None


        

