import threading
import queue

class PwdConsumer(threading.Thread):

your_list='abc'
for current in xrange(5):
    a= [i for i in your_list]
    for y in xrange(current):
        a=[x+i for i in your_list for x in a]
    complete_list=complete_list+a;
    print(complete_list);


complete_list2=[]
for current in range(3):
    a=[i for i in your_list];
    print a
    for y in range(current):
        b=[]
        for x in a:
            for i in your_list:
                b.append(x+1);
                print(b)
                a = [i for i in b]

    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.queue = queue
        self.condition = condition

    def run(self):
        while(True):
            password = None
            self.condition.acquire()
            try:
                password = self.queue.get(block = False)
                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
            self.condition.release()

            if not password is None:
                print("Testing with '123' = " +str(password.check("123")))
                character='a'
                for ch in range('a','z'):
                    print(ch)

