import time
import httplib, urllib
from flask import request
import requests
import json
import datetime

if __name__ == '__main__':
	#print a
	#a+=1
	garbage=[{'canid':10,'level':10,'areaid':001,'timestamp':str(datetime.datetime.now()),'location':{'xcord':41.41,'ycord':54.23}},{'canid':12,'level':15,'areaid':001,'timestamp':str(datetime.datetime.now()),'location':{'xcord':43.41,'ycord':58.23}}]

	requests.post('http://127.0.0.1:5000/',data=json.dumps(garbage))


