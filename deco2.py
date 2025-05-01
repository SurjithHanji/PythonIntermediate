def start_end_decorator(func):
    def wrapper(*args,**kwargs):
        print("start ")
        res=func(*args,**kwargs)
        print("end")
    return wrapper

@start_end_decorator
def add(x):
    return x+5

# print_name=start_end_decorator(print_name)
res=add(10)
print(res)