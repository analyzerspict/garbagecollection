import googlemaps
import requests
import json
import urllib



def getdistances(currentLocation,baseLocation):

	currentl = currentLocation.values()
	#print currentl
	basel = baseLocation.values()
	#print basel
	#str(currentl[0])+','+str(currentl[1])+
	#+str(basel[0])+','+str(basel[1])
	getVars = {'origins': str(currentl[0])+','+str(currentl[1])+'|18.456810, 73.850033|18.452019, 73.851222|18.458959, 73.844733|18.454912, 73.845951|18.461690, 73.850446|'+str(basel[0])+','+str(basel[1]), 'destinations': str(currentl[0])+','+str(currentl[1])+'|18.456810, 73.850033|18.452019, 73.851222|18.458959, 73.844733|18.454912, 73.845951|18.461690, 73.850446|'+str(basel[0])+','+str(basel[1]),'key':'AIzaSyDm9KoNqugH15tA3l6rYt7zmtUEi3VUcog'}
	
	#return  getVars
	url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

	print getVars
	dist=requests.get(url + urllib.urlencode(getVars))

	a = dist.json()
	p = []
	#print a
	for row in a['rows']:
	    q = [] 
	    for col in row['elements']:
		q.append(col['distance']['text'])
	    p.append(q)
	return p

	        
