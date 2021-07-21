from functools import lru_cache
import time


@lru_cache(maxsize=3)  # It will save the last or latest 5 values
def myfunc(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Running some tasks : ")
    myfunc(1)  # The function will not be saved because this is out of the maxsize of cache function.
    myfunc(3)
    myfunc(
        5)  # myfunc 3, 5, 2 will be stored in the cache of the memory else other functions will take the same time of execution.
    myfunc(2)
    print("Done......Called again !")
    myfunc(3)
    myfunc(5)
    myfunc(2)
    print("Done")
    myfunc(6)  # This will take 6 seconds to run because this value is not saved in the cache of the memory.
    print("All done")

# ------------------------------------------------------------------------------
# To create a cache function taking input from the user the maxsize of the cache function and implement it.

m = int(input("Enter the maxsize of the cache function : "))


@lru_cache(maxsize=m)
def cache_function(x):
    time.sleep(x)
    return x

l = int(input("Enter the number time delay to run the function : "))
cache_function(l)
print("Done....With Playing Audio ")
print("Calling function again ......")
cache_function(l)
print("Done")
