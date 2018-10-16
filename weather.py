import time, datetime
import requests
from twilio.rest import Client
from set import SetData
from analyse import Analyse

class Weather(object):

	def getWeather(self):
		# 设置心知天气的apikey
		# 并构造请求URL
		xinzhi_apikey = "92baytheql6d8eq8"
		url = "https://api.thinkpage.cn/v3/weather/daily.json?key=%s&location=guangzhou&language=zh-Hans&unit=c&start=0&days=5" % xinzhi_apikey

		# 获取天气预报信息
		# 此处只取今天和明天2天的预报
		r = requests.get(url)
		w = r.json()["results"][0]["daily"]
		today = "今天是%s，白天%s，晚上%s，最高气温%s，最低气温%s" % (
		w[0]["date"], w[0]["text_day"], w[0]["text_night"], w[0]["high"], w[0]["low"])
		tomorrow = "明天是%s，白天%s，晚上%s，最高气温%s，最低气温%s" % (
		w[1]["date"], w[1]["text_day"], w[1]["text_night"], w[1]["high"], w[1]["low"])
		message = today + '\n' + tomorrow
		print(message)


	# 输入city_id，发送请求
	def getInfo(self):

		r = requests.get('http://www.weather.com.cn/data/sk/101110101.html')
		r.encoding = 'utf-8'  # 编码

		# r.json()['weatherinfo']['city']

		print('temperature = %s' % r.json()['weatherinfo']['temp'])
		print('humidity =  %s' % r.json()['weatherinfo']['SD'])

		return self







if __name__ == "__main__":
	weather = Weather()
	weather.getWeather()