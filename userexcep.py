class valueTohigherror(Exception):
    pass

class valuetoloweror(Exception):
    def __init__(self, message,value):
        self.message=message
        self.value=value
def test_value(x):
    if x>100:
       raise valueTohigherror('value is too high')
    if x < 5:
        raise valuetoloweror('value is too low')
try:
    test_value(3)
except valueTohigherror as e:
    print(e)

except valuetoloweror as e:
    print(e.message)


