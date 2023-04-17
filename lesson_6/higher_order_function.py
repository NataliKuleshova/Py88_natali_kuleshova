def l_func():
    """
    This is function print name to console (l_func)
    """
    print(l_func.__name__)

def s_func():
    """
    This is function print name to console (s_func)
    """
    print(s_func.__name__)

def t_func():
    """
    This is function print name to console (t_func)
    """
    print(t_func.__name__)


def glav_func(func, n=10):
    for i in range(1,n+1):
        print(i, end=" ")
        func()


glav_func(l_func,3)
glav_func(s_func,5)
glav_func(t_func,10)
glav_func(l_func)
