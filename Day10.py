import time
import threading

#Basic scheduler without a list to prevent too many threads
class job_scheduler():
    #takes a function f and a integer n and calls f after n milliseconds
    def __init__(self):
        pass
    def schedule_job(self,f,n):
        def execute():
            time.sleep(n/1000)
            print(f())
        thread = threading.Thread(target=execute)
        thread.start()

#Scheduler with a list so no thread explosion
class list_job_scheduler():
    #takes a function f and a integer n and calls f after n milliseconds
    def __init__(self):
        self.functions = []
        thread = threading.Thread(target=self.queue)
        thread.start()
        
    def queue(self):
        while True:
            now = time.time()*1000
            for fn, due in self.functions:
                if now > due:
                    print(fn(2,3))
            self.functions = [(fn,due) for (fn, due) in self.functions if due > now]
            time.sleep(0.01)
    
    def delay(self,f,n):
        self.functions.append((f,time.time()*1000+n))


def main():
    def func_add(x=2,y=2):
        return x + y
    basic_scheduler = job_scheduler()
    basic_scheduler.schedule_job(func_add,10)
    list_scheduler = list_job_scheduler()
    list_scheduler.delay(func_add,100)

main()