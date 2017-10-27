"""Application Config"""
import os


MQTT_HOST = os.environ.get("mqtt-host", 'm11.cloudmqtt.com')
MQTT_USER = os.environ.get("mqtt-user", 'zdyyuldx')
MQTT_PWD = os.environ.get("mqtt-pwd", '72gARbKu2b_W')
MQTT_PORT = int(os.environ.get("mqtt-port", 17327))
MQTT_FB_WEBHOOK_TOPIC_NAME = 'fb-posts-updates'
WEB_PORT = int(os.environ.get("PORT", 5000))