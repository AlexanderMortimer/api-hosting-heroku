import datetime
from flask import Flask,jsonify,request
app=Flask(__name__)

@app.route('/')
def up_time_excoino():
    return str(datetime.datetime.now())
for i in range(2):
    print(i)
if __name__=="__main__":
   app.run(debug=True) 

