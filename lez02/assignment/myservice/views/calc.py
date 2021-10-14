from flakon import JsonBlueprint
from flask import Flask, request, jsonify

calc = JsonBlueprint('calc', __name__)

@calc.route('/calc/sum', methods=['GET'])
def sum():
	m = int(request.args.get('m'))
	n = int(request.args.get('n'))

	result = m
	if n < 0:
		for i in range(abs(n)):
			result -= 1
	else:
		for i in range(n):
			result += 1

	return jsonify({'result':str(result)})

@calc.route('/calc/div', methods=['GET'])
def div():
	m = int(request.args.get('m'))
	n = int(request.args.get('n'))

	result = -1
	if n==0:
		return jsonify({'result':'Impossible'})
	negative = m > 0 and n < 0 or m < 0 and n > 0
	m = abs(m)
	n = abs(n)
	while m>=0:
		m-=n
		result+=1

	if negative:
		result *= -1

	return jsonify({'result':str(result)})
