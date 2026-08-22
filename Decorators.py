#most basic decorator with out any arguments 

def debug(func):
    def wrapper():
        print("calling funtion:",func.__name__)
        return func()
    return wrapper  # decorator created 

@debug #decorator called
def hello():
    print("Hello")

hello() # funtion called throygh decorator now when hello() is called first debug will bw called then hello()


# #write a decorator that measures the time funtion takes to execute 
import time

def timer(func):
    def wrapper(*args,**kwargs):  #*args means unlimited arguments taken 
        start = time.time()
        result= func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start}time")
        return result
    return wrapper

@timer
def example_funtion(n):
    time.sleep(n)

example_funtion(2)

#create a decorator to print the funtion name and the value of its arguments every time the funtion is called 

def debug(func):
    def wrapper(*args,**kwargs):
        args_value= ', '.join(str(arg)for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling:{func.__name__}with args {args_value}and kwargs{kwargs_value}")
        return func(*args,**kwargs)
    
    return wrapper

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting},{name}")

greet("kesa hai be ", greeting="Mast bhai") # basic funtion created 


