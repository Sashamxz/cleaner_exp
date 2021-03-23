import time
def decoratorr(main_function):
    def time_f():
        start_time= time.time()
        print("start")
        main_function()
        print("time =%s" %(time.time()- start_time) )
    return time_f    

@decoratorr
def king():
    a = [i*i for i in range(0, 10)]
    print(a) 

king()