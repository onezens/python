
#encoding=utf8

class People(object):
	country = "China"

	@staticmethod

	def getCountry():
		return People.country


print(People.getCountry())