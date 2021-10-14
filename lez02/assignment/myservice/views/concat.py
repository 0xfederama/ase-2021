from flakon import JsonBlueprint
from flask import Flask, request, jsonify

concat = JsonBlueprint('concat', __name__)

@concat.route('/concat', methods=['GET'])
def conc():
	m = str(request.args.get('m'))
	n = str(request.args.get('n'))

	return jsonify({'result':str(m+n)})