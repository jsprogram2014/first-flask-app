from flask import Flask,jsonify,request
import json

app=Flask(__name__)
app.config.from_file("config.json",load=json.load)

@app.route('/',methods=['POST','GET'])
def helloworld():
    if request.method=='GET':
        print('this is the ' , request.is_secure )
        print('this is the server host no.',request.headers)
        
        return "<b>You have reached the get method</b>"
    
    return '<b>Welcome new comer hello</b>'

@app.route('/json')
def jsonreturner():
    course=request.args['course'] ## this is a bad way since server will show an error when it doesnt see course
    rating=request.args.get('rating') ## this is a good way since server will return nothing
 
    return {"message":f'This is ur Course {course} and its rating {rating}'}

@app.route('/jsonify')
def jsonifymethod():
    return jsonify(message="hekko jsonify messi or")   