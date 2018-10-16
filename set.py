import xlwt
import xlrd
import datetime


class SetData(object):

	def __init__(self, temperature, humidity):
		self._temperature = temperature
		self._humidity = humidity

	def _open(self, name):
		path = '/Python/Code/data.xls'
		data = xlrd.open_workbook(path)

		sheets = data.sheets()
		if name == 'date':
			sheet_by_name = data.sheet_by_name(u'date')
		elif name == 'temperature':
			sheet_by_name = data.sheet_by_name(u'temperature')
		elif name == 'humidity':
			sheet_by_name = data.sheet_by_name(u'humidity')

		return sheet_by_name

	def write(self):

		i = self._getLength()

		date = []
		temperature = []
		humidity = []

		for j in range(0, i):
			date.append(self._open('date').row_values(j)[0])
			temperature.append(self._open('temperature').row_values(j)[0])
			humidity.append(self._open('humidity').row_values(j)[0])

		#   创建Excel工作表
		workbook = xlwt.Workbook(encoding='ascii')
		worksheet_date = workbook.add_sheet('date')
		worksheet_temperature = workbook.add_sheet('temperature')
		worksheet_humidity = workbook.add_sheet('humidity')

		workbook.save('data.xls')

		for j in range(0, len(date)):
			worksheet_date.write(j, 0, date[j])

		worksheet_date.write(i, 0, self._getTime())

		for j in range(0, len(temperature)):
			worksheet_temperature.write(j, 0, temperature[j])

		worksheet_temperature.write(i, 0, self._temperature)

		for j in range(0, len(humidity)):
			worksheet_humidity.write(j, 0, humidity[j])

		worksheet_humidity.write(i, 0, self._humidity)
		workbook.save('data.xls')

	def _getTime(self):
		raw_day = str(datetime.datetime.now().strftime('%D')).split('/')
		day = int(raw_day[1])

		return day

	def _getLength(self):
		assert self._lengthCheck() == True, \
			'length error, check data.xls'

		#   文件路径
		path = '/Python/Code/data.xls'
		data = xlrd.open_workbook(path)

		#   读入Excel
		sheet_date = data.sheet_by_name(u'date')
		length = sheet_date.nrows

		return length


	#   检查excel长度是否一致
	def _lengthCheck(self):
		path = path = '/Python/Code/data.xls'
		data = xlrd.open_workbook(path)

		#   读入Excel
		sheet_date = data.sheet_by_name(u'date')
		sheet_temperature = data.sheet_by_name(u'temperature')
		sheet_humidity = data.sheet_by_name(u'humidity')

		length_date = sheet_date.nrows
		length_temperature = sheet_temperature.nrows
		length_humidity = sheet_humidity.nrows

		if length_date == length_temperature == length_humidity:
			return True
		else: return False
