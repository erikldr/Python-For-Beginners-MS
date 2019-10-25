def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done Lgoggin')
    return wrapper

@logger
def sampler():
    print('-- Inside sample function')
sampler()