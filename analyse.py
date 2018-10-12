import xlwt
import xlrd
import datetime


class Set_data:

	def __init__(self, temperature, humidity):
		self.__temperature = temperature
		self.__humidity = humidity



	def __open(self, name):
		path = '/Python/Code/data.xls'
		data = xlrd.open_workbook(path)

		sheets = data.sheets()
		if name == 'date':
			sheet_1_by_name = data.sheet_by_name(u'date')
		elif name == 'temperature':
			sheet_1_by_name = data.sheet_by_name(u'temperature')
		elif name == 'humidity':
			sheet_1_by_name = data.sheet_by_name(u'humidity')

		return sheet_1_by_name


	def write(self):

		i = self.__getLength()

		date = []
		temperature = []
		humidity = []

		for j in range(0, i):
			date.append(self.__open('date').row_values(j)[0])
			temperature.append(self.__open('temperature').row_values(j)[0])
			humidity.append(self.__open('humidity').row_values(j)[0])

		#   创建Excel工作表
		workbook = xlwt.Workbook(encoding='ascii')
		worksheet_date = workbook.add_sheet('date')
		worksheet_temperature = workbook.add_sheet('temperature')
		worksheet_humidity = workbook.add_sheet('humidity')

		workbook.save('data.xls')

		for j in range(0, len(date)):
			worksheet_date.write(j, 0, date[j])

		worksheet_date.write(i, 0, self.__getTime())

		for j in range(0, len(temperature)):
			worksheet_temperature.write(j, 0, temperature[j])

		worksheet_temperature.write(i, 0, self.__temperature)

		for j in range(0, len(humidity)):
			worksheet_humidity.write(j, 0, humidity[j])

		worksheet_humidity.write(i, 0, self.__humidity)
		workbook.save('data.xls')


	def __getTime(self):
		day = str(datetime.datetime.now().strftime('%D'))

		return day


	def __getLength(self):
		#   文件路径
		path = '/Python/Code/data.xls'
		data = xlrd.open_workbook(path)

		#   读入Excel
		sheet_1_by_name = data.sheet_by_name(u'date')
		length = sheet_1_by_name.nrows
		print(length)
		return length


