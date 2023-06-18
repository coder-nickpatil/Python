import time

Initial=time.time()
# print(Initial)
k=0
while (k<4):
    print("Nikhil is Best..")
    time.sleep(1)
    k+=1
After_While=time.time()
print("Time:",After_While-Initial)

for i in range(5):
    print("Nikhil is Good Boy..")
After_for=time.time()
print("Time:",After_for-Initial)

localtime=time.asctime(time.localtime(time.time()))
print(localtime)