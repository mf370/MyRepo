import redis
import json
import random
import time
from lib import RedisQueue
from readCSV import readFile


q = RedisQueue('123')
q.put(readFile("avioes2.csv"))
#q.putJSON("avioesJSON.json")

#i = 1
#while i < 10001:
    #msg = 'manel - ' + str(i)
    #q.put(msg)
    #i += 1

#a = RedisQueue('maria')
#v = a.put2("cenas")

#print(v)