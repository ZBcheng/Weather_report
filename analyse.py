import xlrd
import matplotlib.pyplot as plt

class Analyse(object):
	def __init__(self, path):
		self.__path = path
		self.__list_date = []
		self.__list_temperature_low = []
		self.__list_temperature_high = []


	def __createList(self):
		data = xlrd.open_workbook(self.__path)

		#   读入Excel
		sheet_date = data.sheet_by_name(u'date')
		sheet_temperature_low = data.sheet_by_name(u'temperature_low')
		sheet_temperature_high = data.sheet_by_name(u'temperature_high')

		length_date = sheet_date.nrows
		length_temperature_low = sheet_temperature_low.nrows
		length_temperature_high = sheet_temperature_high.nrows

		for i in range(0, length_date):
			self.__list_date.append(sheet_date.row_values(i))

		for i in range(0, length_temperature_low):
			self.__list_temperature_low.append(sheet_temperature_low.row_values(i))

		for i in range(0, length_temperature_high):
			self.__list_temperature_high.append(sheet_temperature_high.row_values(i))

		return length_date


	def createPic(self):
		self.__createList()
		date = []
		temperature_low = []
		temperature_high = []

		for i in range(0, len(self.__list_date)):
			date.append(self.__list_date[i][0])
			temperature_low.append(self.__list_temperature_low[i][0])
			temperature_high.append(self.__list_temperature_high[i][0])

		plt.xlabel('Date')
		plt.ylabel('Temperature')

		#   添加日期与温度关系
		plt.plot(date, temperature_low, color='b', label='temperature_low')
		plt.plot(date, temperature_high, color='r', label='temperature_high')

		plt.legend(loc='upper left')
		plt.show()

