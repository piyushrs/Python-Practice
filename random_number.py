import random
import time

while(True):
    print(random.randrange(1,25))
    time.sleep(2)
# import pathlib
# import datetime

# folder_path = "D:/Practice"

# for i,j,k in pathlib.os.walk(folder_path):
#     # print(pathlib.os.path.join(i,k))
#     for filename in k:
#         print(pathlib.os.path.join(i,filename))

# res = [pathlib.os.path.join(i,filename) for i,j,k in pathlib.os.walk(folder_path) for filename in k]
# # print(*res + "created at: " + datetime.datetime.fromtimestamp(pathlib.Path(*res).stat().st_ctime), sep = '\n')
# print(*res, sep = '\n')