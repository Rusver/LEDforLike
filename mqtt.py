"""This module exposes a class that handles all MQTT interactions"""
import logging
import json
import paho.mqtt.client as paho

# pylint: disable=too-few-public-methods

class MqttClient:
    """A facade api to  MQTT client"""

    def __init__(self):
        self.mqttc = paho.Client()
        self.mqttc.username_pw_set(os.environ('MQTT_USER'),os.environ('MQTT_PWD'))

        logging.warning(
            'Trying to establish connection to ' + os.environ('MQTT_HOST'))
        try:
            self.mqttc.connect(os.environ('MQTT_HOST'), os.environ('MQTT_PORT'))
        except ValueError:
            logging.critical(
                "Oops! connection to '%s' couldn't be established", Config.MQTT_HOST)

    """Publishes a new message to a topic"""
    def publish(self, topic, message):
        return self.mqttc.publish(topic, json.dumps(message))
        #return self.mqttc.publish(topic, json.dumps(message))
