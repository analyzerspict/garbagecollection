import time
import httplib, urllib
from flask import request
import threading
from threading import Thread
import requests
import json
import datetime
import random
def start1():
	
	while True:
		
				
		garbage= {'canid':1,'level':random.randint(5,30),'areaid':001,'timestamp':str(datetime.datetime.now()),'xcord':18.456810 ,'ycord':73.850033}
	
	
		requests.post('http://127.0.0.1:5000/sensor',data=json.dumps(garbage))
		time.sleep(2)


def start2():
	
	while True:
		
				
		garbage= {'canid':2,'level':20,'areaid':1,'timestamp':str(datetime.datetime.now()),'xcord':18.452019 ,'ycord':73.851222}
	
	
		requests.post('http://127.0.0.1:5000/sensor',data=json.dumps(garbage))
		time.sleep(2)


def start3():
	
	while True:
		
				
		garbage= {'canid':3,'level':30,'areaid':1,'timestamp':str(datetime.datetime.now()),'xcord':18.458959  ,'ycord':73.844733}
	
	
		requests.post('http://127.0.0.1:5000/sensor',data=json.dumps(garbage))
		time.sleep(2)



def start4():
	
	while True:
		
				
		garbage= {'canid':4,'level':40,'areaid':1,'timestamp':str(datetime.datetime.now()),'xcord':18.454912  ,'ycord':73.845951}
	
	
		requests.post('http://127.0.0.1:5000/sensor',data=json.dumps(garbage))
		time.sleep(2)



def start5():
	
	while True:
		
				
		garbage= {'canid':5,'level':50,'areaid':1,'timestamp':str(datetime.datetime.now()),'xcord':18.461690,  'ycord':73.850446}
	
	
		requests.post('http://127.0.0.1:5000/sensor',data=json.dumps(garbage))
		time.sleep(2)



if __name__=="__main__":
	Thread(target=start1).start()
	Thread(target=start2).start()
	Thread(target=start3).start()
	Thread(target=start4).start()	
	Thread(target=start5).start()
