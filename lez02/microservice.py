from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST', 'DELETE', 'GET'])
def my_microservice():
	return jsonify({'Hello','World'})

@app.route('/api/person/<person_id>')
def person(person_id):
	response = jsonify({'Hello': person_id})
	return response

if __name__ == '__main__':
	app.run()
