from flask import Flask
from flask import json
from flask import Response
from flask import request
import os
import logging
import settings as Config
from mqtt import MqttClient
from msg import Msg

"""Server class"""
class Server(object):
	app = Flask(__name__)
	MQTTC = MqttClient()

	@app.route("/", methods =['GET', 'POST'])
	def Welcome():
		return "Welcome to my page :)"

	@app.route('/articles')
	def api_articles():
		return 'List of articles'

	@app.route('/articles/<articleid>')
	def api_article(articleid):
		return 'You are reading ' + articleid

	@app.route('/json', methods = ['GET', 'POST'])
	def api_json():
		data = {k:v for k,v in request.args.items()}
		return json.dumps(data)

	@app.route('/hello', methods = ['GET', 'POST'])
	def api_hello():
		data = {
			'hello'  : 'world',
			'number' : 3
		}
		return json.dumps(data)

	"""webhook api"""
	@app.route("/webhook", methods=['GET'])
	def verify():
		return request.args.get('hub.challenge')

	@app.route("/webhook", methods=['POST'])
	def fb_feeds_webhook():
		"""webhook api"""
		logging.debug('Handling webhook request!!')
		content = request.get_json()
		if content['entry'][0]['changes'][0]['value']['item'] == 'like':
			Server.MQTTC.publish(
				Config.MQTT_FB_WEBHOOK_TOPIC_NAME, Msg(
					int(content['entry'][0]['time']),'LIKE',
					content['entry'][0]['changes'][0]['value']['user_id']))
		
		logging.info('Handled webhook request ' + str(content))
		return ''
		
	if __name__ == '__main__':
		app.debug = True
		app.run(host = '0.0.0.0', port = int(os.environ.get("PORT", 5000)))
