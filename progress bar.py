import time
from tqdm import tqdm
mylist = [1]
a = 10
for i in range(a):
    for j in tqdm(mylist):
        # print("hello")
        time.sleep(1)
