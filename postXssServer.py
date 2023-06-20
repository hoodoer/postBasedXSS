#!/usr/bin/env python

from flask import Flask, make_response, request, jsonify


app = Flask(__name__)



def printHeader():
	print("""                                  
 __ __  _____ _____                                                
|  |  |/ ___// ___/                                                
|  |  (   \_(   \_                                                 
|_   _|\__  |\__  |                                                
|     |/  \ |/  \ |                                                
|  |  |\    |\    |                                                
|__|__| \___| \___|                                                
                                                                   
  ____  _      _                                                   
 /    || |    | |                                                  
|  o  || |    | |                                                  
|     || |___ | |___                                               
|  _  ||     ||     |                                              
|  |  ||     ||     |                                              
|__|__||_____||_____|                                              
                                                                   
 ______  __ __    ___      ______  __ __  ____  ____    ____  _____
|      ||  |  |  /  _]    |      ||  |  ||    ||    \  /    |/ ___/
|      ||  |  | /  [_     |      ||  |  | |  | |  _  ||   __(   \_ 
|_|  |_||  _  ||    _]    |_|  |_||  _  | |  | |  |  ||  |  |\__  |
  |  |  |  |  ||   [_       |  |  |  |  | |  | |  |  ||  |_ |/  \ |
  |  |  |  |  ||     |      |  |  |  |  | |  | |  |  ||     |\    |
  |__|  |__|__||_____|      |__|  |__|__||____||__|__||___,_| \___|
                                                                   

                     @hoodoer
               https://trustedsec.com
		""")



#Index page
@app.route('/', methods=['GET'])
def index():
	with open('./src/index.src', 'r') as file:
		page = file.read()
		response = make_response(page, 200)
		response.mimetype = 'text/html'

	return response


# Method
@app.route('/methodTamper', methods=['GET'])
def methodForm():
	with open('./src/method.src', 'r') as file:
		page = file.read()
		response = make_response(page, 200)
		response.mimetype = 'text/html'

	return response


@app.route('/postForm', methods=['GET', 'POST'])
def receiveForm():
	firstName = request.values['fname']
	lastName = request.values['lname']
	print("Got names: " + firstName + ' ' + lastName)
	response = make_response('<h1>Welcome!</h1><p>' + firstName + ' ' + lastName + 
		'</p><br><a href="javascript:history.back()">Go Back</a>', 200)

	return response



#CSRF
@app.route('/csrf', methods=['GET'])
def csrfPage():
	with open('./src/csrf.src', 'r') as file:
		page = file.read()
		response = make_response(page, 200)
		response.mimetype = 'text/html'

	return response


@app.route('/csrfPostForm', methods=['POST'])
def receiveCSRFForm():
	firstName = request.form['fname']
	lastName = request.form['lname']
	print("Got names: " + firstName + ' ' + lastName)
	response = make_response('<h1>Welcome!</h1><p>' + firstName + ' ' + lastName + 
		'</p><br><a href="javascript:history.back()">Go Back</a>', 200)

	return response



# #CORS
# @app.route('/cors', methods=['GET'])
# def corsPage():
# 	with open('./src/cors.src', 'r') as file:
# 		page = file.read()
# 		response = make_response(page, 200)
# 		response.mimetype = 'text/html'

# 	return response


# @app.route('/corsPost', methods=['POST'])
# def receiveCORSPost():
# 	firstName = request.json.get('fname')
# 	lastName = request.json.get('lname')
# 	print("Got names: " + firstName + ' ' + lastName)
# 	response = make_response('Welcome ' + firstName + ' ' + lastName + 
# 		'<br><a href="javascript:history.back()">Go Back</a>', 200)

# 	return response


#CORS
@app.route('/fakeJson', methods=['GET'])
def corsPage():
	with open('./src/fakeJson.src', 'r') as file:
		page = file.read()
		response = make_response(page, 200)
		response.mimetype = 'text/html'

	return response


@app.route('/fakeJsonPost', methods=['POST'])
def receiveFakeJsonPost():
	# data1 = request.get_data()
	# print("** Raw data: " + data1)

	# data = jsonify(request.get_json(force=True))
	# data = jsonify(request.get_data(force=True))
	data = request.get_data().decode()
	print("** Raw data: " + data)
	parsed = jsonify(data)

	print(type(parsed))

	# firstName = data.json.get('fname')
	# # lastName = request.json.get('lname')
	# firstName = parsed.json.g('fname')
	# # # lastName = request.json.get('lname')

	# print("Got name: " + firstName)
	# response = make_response('Welcome ' + firstName + 
	# 	'<br><a href="javascript:history.back()">Go Back</a>', 200)

	return 200




if __name__ == '__main__':
	printHeader()
	app.run(debug=False, host='0.0.0.0', port=80)
	
