import time
import random
from functools import wraps


def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry

@retry(Exception, tries=4)
def test_random(text):
    x = random.random()
    if x < 0.5:
        raise Exception("Fail")
    else:
        print("Success: ", text)

test_random("it works!")

list_instance = [1, 2, 3, 4]
print(iter(list_instance))

# instanciar iterable
list_instance = [1, 2, 3, 4]
print(list_instance)

# producir un iterador a partir de un iterable
iterator = iter(list_instance)
print(list(iterator))