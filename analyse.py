import xlrd
import matplotlib.pyplot as plt

class Analyse:
	def __init__(self, path):
		self.__path = path

		self.__list_date = []
		self.__list_temperature = []
		self.__list_humidity = []


	def __createList(self):
		data = xlrd.open_workbook(self.__path)

		#   读入Excel
		sheet_date = data.sheet_by_name(u'date')
		sheet_temperature = data.sheet_by_name(u'temperature')
		sheet_humidity = data.sheet_by_name(u'humidity')

		length_date = sheet_date.nrows
		length_temperature = sheet_temperature.nrows
		length_humidity = sheet_humidity.nrows

		for i in range(0, length_date):
			self.__list_date.append(sheet_date.row_values(i))

		for i in range(0, length_temperature):
			self.__list_temperature.append(sheet_temperature.row_values(i))

		for i in range(0, length_humidity):
			self.__list_humidity.append(sheet_humidity.row_values(i))

		return length_date

	def createPic(self):
		self.__createList()
		plt.scatter(self.__list_date, self.__list_temperature)
		plt.show()