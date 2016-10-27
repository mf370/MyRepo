from lib import RedisQueue
import threading
import csv
import json
import codecs

def consumidor():
    c = RedisQueue("123")
    a = c.getatomic()
    print(a)

#n = int(input("Insert thread number: "))

def main():
    threads = []
    for i in range(20):
        threads.append(threading.Thread(target=consumidor))
    for thread in threads:
        thread.start()
    for index, thread in enumerate(threads):
        if thread.is_alive():
            print("Thread " + str(index) + " still running")
    for thread in threads:
        thread.join()

#main()


def consumidor2():
    c = RedisQueue("123")
    redisqueue = c.get()
    decodedData = redisqueue.decode("utf-8") #transforma o tipo de dados de bytes para str, o json so le str
    json_data = json.loads(decodedData)
    #print(json_data)

    keys = json_data[0].keys()
    with open('avioes2copia.csv', 'w', newline='') as escritor:
        csvEscritor = csv.DictWriter(escritor,keys)
        csvEscritor.writeheader()
        csvEscritor.writerows(json_data)

#keys = toCSV[0].keys()
#with open('people.csv', 'wb') as output_file:
    #dict_writer = csv.DictWriter(output_file, keys)
    #dict_writer.writeheader()
    #dict_writer.writerows(toCSV)


consumidor2()
