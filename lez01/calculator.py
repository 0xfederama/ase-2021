import calc as c

class Calculator:

	def __init__(self):
		pass

	def sum(self, m, n):
		return c.sum(m, n)

	def divide(self, m, n):
		return c.divide(m, n)

calc = Calculator()
print(calc.sum(5, -3))
print(calc.divide(9, -2))