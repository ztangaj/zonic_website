from flask import Flask , render_template, request, Response, jsonify, abort
import requests
import json

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return  render_template('index.html')
#	return ("hello world!!")

@app.route('/about',methods = ['GET'])
def about():
    return  render_template('about.html')

@app.route('/panel',methods = ['GET','POST'])
def panel():
    if request.method == 'POST':
        if request.form['submit_button']== '開燈':
            print("Open")
            url = 'http://zonicspaceworkshop.com/Iot/Light'
            data = {'Switch':'Open'}
            headers = {'Content-Type': 'application/json'}
            requests.post(url, data=json.dumps(data),headers = headers)
            return render_template('panel.html')
        elif request.form['submit_button']=='關燈':
            url = 'http://zonicspaceworkshop.com/Iot/Light'
            data = {'Switch':'Close'}
            headers = {'Content-Type': 'application/json'}
            requests.post(url, data=json.dumps(data),headers = headers)
            return render_template('panel.html')
            #return ("Close")
    elif request.method == 'GET':
        return render_template('panel.html')

#webhook Iot
@app.route('/Iot/AC',methods = ['POST','GET'])
def respond_AC():
    if request.method == 'POST':
        try:
            output = request.get_json(force=True)
            print(output)
            global output_global_ac
            output_global_ac = output
        except:
            abort(400)
        return jsonify(output)
    else:
        try:
            print(output_global_ac)
            return jsonify(output_global_ac)
        except:
            output = {"Switch": "None"}
            #return ("No request")
            print(output)
            return jsonify(output)

@app.route('/Iot/Light',methods = ['POST','GET'])
def respond_Light():
    if request.method == 'POST':
        try:
            output = request.get_json(force=True)
            print(output)
            global output_global_light
            output_global_light = output
        except:
            abort(400)
        return jsonify(output)
    else:
        try:
            print(output_global_light)
            return jsonify(output_global_light)
        except:
            output = {"Switch": "None"}
            #return ("No request")
            print(output)
            return jsonify(output)
#curl -X POST -H "Content-Type: application/json" -d '{"Switch" : "Open"}' "http://zonicspaceworkshop.com/Iot/Light"


if __name__ == '__main__':
    app.run(port = 5000, debug= True)
	#application.run()
