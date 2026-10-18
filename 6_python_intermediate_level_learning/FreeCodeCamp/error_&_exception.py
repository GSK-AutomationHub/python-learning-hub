
class ValueTooHighException(Exception):
    pass

class ValueTooSmallException(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def value_test(value):
    if value > 100:
        raise ValueTooHighException('value is out of max limit')
    elif value < 0:
        raise ValueTooSmallException('value is out of min limit', value)
    else:
        print('test passed')


def main(value):
    try:
        value_test(value)
    except ValueTooSmallException as e:
        print(e.message)
        print(e.value)
    except ValueTooHighException as e:
        print(e)
    else:
        print('all run well')
    finally:
        print('cleaning up....')
    


if __name__ == "__main__":
    main(-2)
else:
    print('main fucntion is not for outside use')
