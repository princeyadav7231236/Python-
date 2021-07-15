import time
sec = time.time()
print(sec)

current_time = time.asctime()
print(current_time)
a = time.localtime()
print(a)


initial = time.time()
k = 0
while k < 5:
    print("This is DEVIL")
    time.sleep(2)
    k += 1

print("While loop", time.time()-initial, "seconds")

initial2 = time.time()
for i in range(5):
    print("This is me")

print("for loop ", time.time()-initial2, "seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
