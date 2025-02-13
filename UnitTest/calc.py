
def add(x,y):
    """ Adding Function """
    return x + y

def substract(x,y):
    """ Substracting Function"""
    return x - y

def multipy(x,y):
    """ Multiplication Function """
    return x * y

def divide(x,y):
    """ Dividing Function"""
    if y == 0:
        raise ValueError("Division by 0 not allowed")
    else:
        return x/y

if __name__ == '__main__':
    output = multipy(5,10)
    print(output)