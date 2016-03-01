from flask import Flask,request,render_template
import json
from connection import Database,CONNECTION_STRING,DATABASE_NAME,GARBAGE_CANS_COLLECTION
import pymongo


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        print 'request received'
        content = json.loads(request.data)
        print content
        print type(content)
        b = d.collection.insert_many(content)
        return json.dumps(str(b))

def database_setup():
    global d
    d = Database(CONNECTION_STRING)
    d.connect_to_database(DATABASE_NAME)
    d.connect_to_collection(GARBAGE_CANS_COLLECTION)

if __name__ == '__main__':
    database_setup()
    app.run(host='127.0.0.1',debug=True)
