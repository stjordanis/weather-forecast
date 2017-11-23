from kafka import KafkaProducer
#from .settings import BOOTSTRAP_SERVER, TOPIC_NAME
import logging
import os
from datetime import datetime
from weather_client.transformer import Transformer
logging.basicConfig(level=logging.DEBUG)


BOOTSTRAP_SERVER = "172.17.0.1"
#BOOTSTRAP_SERVER = "kafka"


TOPIC_NAME = "test"
WEATHER_API_URL = ""

class WeatherClient(object):

    def __init__(self, records):
        self._records = records

    def run(self):

        #logging.critical("----------start processing-------")
        #logging.info(self._records)
        # raw_records = HTTP.request(WEATHER_API_URL)
        transformer = Transformer(self._records)
        transformed_records = transformer.run()
        producer =  KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVER])
        producer.send(TOPIC_NAME, b'raw_bytes')
        metrics = producer.metrics()
        logging.info(metrics)
        logging.critical("----------end processing-------")




