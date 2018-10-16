import time, datetime
import requests
from twilio.rest import Client
from set import SetData
from analyse import Analyse

class Weather(object):

	def __init__(self, phone_number, start_time):

		assert type(phone_number) is str, \
			'the type of phone_number should be str'
		assert start_time < 2400, \
			'must set a time before 24:00'

		self._phone_number = phone_number
		self._start_time = start_time


	def _getInfo(self):

		# 设置心知天气的apikey
		# 并构造请求URL
		xinzhi_apikey = "92baytheql6d8eq8"
		url = "https://api.thinkpage.cn/v3/weather/daily.json?key=%s&location=xian&language=zh-Hans&unit=c&start=0&days=5" % xinzhi_apikey

		# 获取天气预报信息
		# 此处只取今天和明天2天的预报
		r = requests.get(url)
		weather = r.json()["results"][0]["daily"]

		info = 'Good morning Bee!\n' + "Temperature in Xi'an: " + weather[0]['low'] + '-' + weather[0]['high']

		total = [info, weather[0]['high'], weather[0]['low']]

		return total
	'''
	# 输入city_id，发送请求
	def _getInfo(self):

		r = requests.get('http://www.weather.com.cn/data/sk/' + str(self._city_id) + '.html')
		r.encoding = 'utf-8'  # 编码

		# r.json()['weatherinfo']['city']

		temperature = r.json()['weatherinfo']['temp']
		humidity = r.json()['weatherinfo']['SD']
		list = ["Weather in Xi'an:", "Temperature:  " + temperature,
		        "Humidity:  " + humidity]

		data = str(list[0] + '\n' + list[1] + '\n' + list[2])
		info = 'Good morning Bee!\n' + data


		total = [info, temperature, humidity.split('%')[0]]

		return total
	'''


	# 发送短信
	def _send(self):
		self._setTime()

		account_sid = 'AC7c4003f4b37c35d2e4249984df784b69'
		auth_token = '6345546fae4ad92e602570250760c0fe'
		client = Client(account_sid, auth_token)

		message = client.messages.create(
			body = self._getInfo()[0],
			from_ = '(239) 237-3586',
			to = self._phone_number
		)

		info = SetData(self._getInfo()[1], self._getInfo()[2])
		print(self._getInfo()[0])
		info.write()
		x = Analyse('/Python/Code/data.xls')
		x.createPic()
		time.sleep(70)

		#print(message.sid)


	def start(self):
		while(True):
			self._send()

	# 设置获取时间
	def _setTime(self):

		# 获取当前小时与分钟
		now = str(datetime.datetime.now().strftime('%H') + datetime.datetime.now().strftime('%M'))

		# 转换为整型
		cur = int(now)

		print('Program not starting yet...')

		# 比较设定时间与当前时间
		while cur != self._start_time:
			now = str(datetime.datetime.now().strftime('%H') + datetime.datetime.now().strftime('%M'))
			cur = int(now)
			time.sleep(1)

		print('starting')

