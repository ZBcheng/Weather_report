import xlrd
import matplotlib.pyplot as plt

class Analyse(object):
	def __init__(self, path):
		self._path = path
		self._list_date = []
		self._list_temperature = []
		self._list_humidity = []


	def _createList(self):
		data = xlrd.open_workbook(self._path)

		#   读入Excel
		sheet_date = data.sheet_by_name(u'date')
		sheet_temperature = data.sheet_by_name(u'temperature')
		sheet_humidity = data.sheet_by_name(u'humidity')

		length_date = sheet_date.nrows
		length_temperature = sheet_temperature.nrows
		length_humidity = sheet_humidity.nrows

		for i in range(0, length_date):
			self._list_date.append(sheet_date.row_values(i))

		for i in range(0, length_temperature):
			self._list_temperature.append(sheet_temperature.row_values(i))

		for i in range(0, length_humidity):
			self._list_humidity.append(sheet_humidity.row_values(i))

		return length_date

	def createPic(self):
		self._createList()
		for i in range(0, len(self._list_date)):
			plt.scatter(self._list_date[i], self._list_temperature[i], color='red')
			plt.scatter(self._list_date[i], self._list_humidity[i], color='blue')
		plt.show()

