from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/')
def helloworld():
    return '<b>Welcome new comer hello</b>'

@app.route('/json')
def jsonreturner():
    return {"message":'hekki json'}

@app.route('/jsonify')
def jsonifymethod():
    return jsonify(message="hekko jsonify")