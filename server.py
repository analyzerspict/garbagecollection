from flask import Flask,request,render_template,redirect,url_for
import  json
import connection
import pymongo
import distancematrix
import brute





app = Flask(__name__)

a = '' 	#just used to give a name to the database and pass it as a parameter

B='success'



#startup page
@app.route('/',methods=['GET','POST'])
def view_homepage():
	if request.method=='GET':
		return (render_template('index.html'))
	
#login page gets loaded		
@app.route('/Loginpage',methods=['GET','POST'])
def view_Loginpage():
	return (render_template('Loginpage.html'))
			
		

#sign up  page gets loaded		
@app.route('/SignUpPage',methods=['GET','POST'])
def view_SignUpPage():
	return (render_template('SignUpPage.html'))



#dashboard  page gets loaded		
@app.route('/Analyzers/Dashboard',methods=['GET','POST'])
def view_Dashboard():
	return (render_template('Dashboard.html'))

		
		
#login activity
@app.route('/login',methods=['GET','POST'])
def login_auth():
	error=None
	if request.method=='POST':
		usr ,passwd= connection.get_auth_details(a)
		print usr , '       ' , passwd
		if request.form['username']!=str(usr) and request.form['password']!=str(passwd):
			error="Invalid credentials.Please try again"
			
		else:
			print 'success'
			return redirect(url_for('view_Dashboard'))
	return redirect(url_for('view_Loginpage',error=error))
			
			
			

	





#all the data from the sensors are received at this endpoint and then stored in the data base
@app.route('/sensor',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
	print 'success'
	content = json.loads(request.data)
	print content
	
        #v = request.form['string']
        b = connection.insert__sensor_document(content,a)
	return json.dumps(str(b))



@app.route('/location',methods=['GET','POST'])
def getLocation():
    if request.method=='POST':
        location=json.loads(request.data)
	return 'success'
	 







#we get the distance matrix here an apply TSP to get the sequence of the indices to be visited 
@app.route('/tsp/<areaid>',methods=['GET','POST'])
def calculate(areaid):
	if request.method == 'POST':
		
		collector = json.loads(request.data)	
		#print areaid
		matrix=distancematrix.getdistances(collector['currentLocation'], collector['baseLocation'])
		#print matrix
		can_level_list=[]
		for i in range(1,6):
			level=connection.get_document(areaid,a,i)
			
			can_level_list.append(level)
		print can_level_list
		
		
		sequence=brute.calculate_path(matrix,can_level_list)  #calculate path
		seq_content={'sequence': str(sequence)}
		insert_seq=connection.insert_sequence_document(seq_content,a)   #store the sequence in the database
	return 'success'




#javaScript browser client will send get request at this endpoint. for demo try out the a.py  available on desktop
@app.route('/sequence',methods=['GET','POST'])
def return_sequnce():
	if request.method=='GET':
	
		seq=connection.get_sequence(a)
		return seq
	



					

if __name__ == '__main__':
    a = connection.database_setup()

    app.run(host='0.0.0.0',debug=True)
