import time, datetime
import requests
from twilio.rest import Client


class Weather:

	def __init__(self, phone_number, city_id, start_time):

		assert type(phone_number) is str, \
			'the type of phone_number should be str'
		assert start_time < 2400, \
			'must set a time before 24:00'

		self.__phone_number = phone_number
		self.__city_id = city_id
		self.__start_time = start_time


	# 输入city_id，发送请求
	def __getInfo(self):

		r = requests.get('http://www.weather.com.cn/data/sk/' + str(self.__city_id) + '.html')
		r.encoding = 'utf-8'  # 编码

		# r.json()['weatherinfo']['city']
		list = ["Weather in Xi'an:", "Temperature:  " + r.json()['weatherinfo']['temp'],
		        "Humidity:  " + r.json()['weatherinfo']['SD']]

		data = str(list[0] + '\n' + list[1] + '\n' + list[2])
		info = 'Good morning Bee!\n' + data

		print(info)

		return info


	# 发送短信
	def send(self):
		self.__setTime()
		account_sid = 'AC7c4003f4b37c35d2e4249984df784b69'
		auth_token = '6345546fae4ad92e602570250760c0fe'
		client = Client(account_sid, auth_token)

		message = client.messages.create(
			body = self.__getInfo(),  # Xi'an city_id
			from_ = '(239) 237-3586',
			to = self.__phone_number
		)

		print(message.sid)


	# 设置获取时间
	def __setTime(self):

		# 获取当前小时与分钟
		now = str(datetime.datetime.now().strftime('%H') + datetime.datetime.now().strftime('%M'))

		# 转换为整型
		cur = int(now)

		print('Program not starting yet...')

		# 比较设定时间与当前时间
		while cur != self.__start_time:
			now = str(datetime.datetime.now().strftime('%H') + datetime.datetime.now().strftime('%M'))
			cur = int(now)
			time.sleep(1)

		print('starting')


if __name__ == '__main__':

	xian = Weather('+8615686442131', 101110101, 2145)

	xian.send()

