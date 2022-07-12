import time


def performance(func):
    def wraper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__+' took '+str((end-start)*1000)+' mil sec')
        return result
    return wraper
