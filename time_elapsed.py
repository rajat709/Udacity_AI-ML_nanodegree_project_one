from time import time, sleep

class TimeElapsed:
    def __init__(self):
        self.start_time = time()
        self.end_time = None
        return

    def get_total_hours(self,tot_time):
        return str(int((tot_time/3600)))
    
    def get_total_minutes(self,tot_time):
        return str(int((tot_time%3600)/60))
    
    def get_total_seconds(self,tot_time):
        return str(round((tot_time%3600)%60)) 
    
    def stop_and_print_time_elapsed(self):
        self.end_time = time()
        tot_time = self.end_time - self.start_time
        print("\n** Total Elapsed Runtime:",
          self.get_total_hours(tot_time)+":"+
              self.get_total_minutes(tot_time)+":"
          +self.get_total_seconds(tot_time))
        return