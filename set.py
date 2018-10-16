import xlwt
import xlrd
import datetime


class SetData(object):

	def __init__(self, temperature_low, temperature_high):
		self.__temperature_low = temperature_low
		self.__temperature_high = temperature_high

	def __open(self, name):
		path = '/Python/Code/data.xls'
		data = xlrd.open_workbook(path)

		sheets = data.sheets()
		if name == 'date':
			sheet_by_name = data.sheet_by_name(u'date')
		elif name == 'temperature_low':
			sheet_by_name = data.sheet_by_name(u'temperature_low')
		elif name == 'temperature_high':
			sheet_by_name = data.sheet_by_name(u'temperature_high')

		return sheet_by_name

	def write(self):

		i = self.__getLength()

		date = []
		temperature_low = []
		temperature_high = []

		for j in range(0, i):
			date.append(self.__open('date').row_values(j)[0])
			temperature_low.append(self.__open('temperature_low').row_values(j)[0])
			temperature_high.append(self.__open('temperature_high').row_values(j)[0])

		#   创建Excel工作表
		workbook = xlwt.Workbook(encoding='ascii')
		worksheet_date = workbook.add_sheet('date')
		worksheet_temperature_low = workbook.add_sheet('temperature_low')
		worksheet_temperature_high = workbook.add_sheet('temperature_high')

		workbook.save('data.xls')

		for j in range(0, len(date)):
			worksheet_date.write(j, 0, date[j])

		worksheet_date.write(i, 0, self.__getTime())

		for j in range(0, len(temperature_low)):
			worksheet_temperature_low.write(j, 0, temperature_low[j])

		worksheet_temperature_low.write(i, 0, self.__temperature_low)

		for j in range(0, len(temperature_high)):
			worksheet_temperature_high.write(j, 0, temperature_high[j])

		worksheet_temperature_high.write(i, 0, self.__temperature_high)
		workbook.save('data.xls')

	def __getTime(self):
		raw_day = str(datetime.datetime.now().strftime('%D')).split('/')
		day = int(raw_day[1])

		return day

	def __getLength(self):
		assert self.__lengthCheck() == True, \
			'length error, check data.xls'

		#   文件路径
		path = '/Python/Code/data.xls'
		data = xlrd.open_workbook(path)

		#   读入Excel
		sheet_date = data.sheet_by_name(u'date')
		length = sheet_date.nrows

		return length


	#   检查excel长度是否一致
	def __lengthCheck(self):
		path = path = '/Python/Code/data.xls'
		data = xlrd.open_workbook(path)

		#   读入Excel
		sheet_date = data.sheet_by_name(u'date')
		sheet_temperature_low = data.sheet_by_name(u'temperature_low')
		sheet_temperature_high = data.sheet_by_name(u'temperature_high')

		length_date = sheet_date.nrows
		length_temperature_low = sheet_temperature_low.nrows
		length_temperature_high = sheet_temperature_high.nrows

		if length_date == length_temperature_low == length_temperature_high:
			return True
		else: return False
