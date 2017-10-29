from flask import Flask
from flask import json
from flask import Response
from flask import request
import os
import logging
from mqtt import MqttClient

"""Server class"""
class Server(object):
	app = Flask(__name__)
	MQTTC = MqttClient()

	@app.route("/", methods =['GET', 'POST'])
	def Welcome():
		return "Welcome to my page :)"


	"""webhook api"""
	@app.route("/webhook", methods=['GET'])
	def verify():
		return request.args.get('hub.challenge')

	@app.route("/webhook", methods=['POST'])
	def fb_feeds_webhook():
		"""webhook api"""
		logging.debug('Handling webhook request!!')
		content = request.get_json()
		print str(content)
		if content['entry'][0]['changes'][0]['value']['item'] == 'like':
			msg = {
				"time" 		: int(content['entry'][0]['time']),
				"topic" 	: "LIKE",
				"user_id" 	: content['entry'][0]['changes'][0]['value']['user_id']
				}
			Server.MQTTC.publish('Facebook', msg)
		
		logging.info('Handled webhook request' + str(content))
		return ''



if __name__ == '__main__':
	Server = Server()
	Server.app.debug = True
	Server.app.run(host = '0.0.0.0', port = int(os.environ.get("PORT", 5000)))
