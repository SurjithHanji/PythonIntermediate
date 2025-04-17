# x=-5
# if x<0:
#     raise Exception('X should be positive')


# y=-5
# assert(y>=0),'x is not positive'

try:
    a=5/0
    b=5+'10'
except Exception as e:
    print(e)
    print('num cant be divide by zero')

except TypeError as e:
    print(e)
    print('typeerror')

else:
    print("everything is fine")

finally:
    print("always for u ")