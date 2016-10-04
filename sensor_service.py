import time
import datetime
import Adafruit_DHT as dht


def get_data():
    try:
        h, t = dht.read_retry(dht.DHT11, 14)
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#        print "%s Temperature: %f*C Humidity: %f%%" % (str(cur_time), t, h)
        return {
            'humidity': h,
            'temperature': t,
            'time': str(cur_time)
        }
    except Exception as ex:
        print ex
