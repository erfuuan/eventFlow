
# print('''
# ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
# ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
# ░▒▓█▓▒░       ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
# ░▒▓██████▓▒░  ░▒▓█▓▒▒▓█▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
# ░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
# ░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
# ░▒▓████████▓▒░  ░▒▓██▓▒░  ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█████████████▓▒░                                                                                                  
#  ''')
print('''
-- ::::::::::::::::::::::::::::::::::::::::::::::::::::::
-- ::::::::::::::::::::::::::::::::::::::::::::::::::::::
-- ::                       _   _____ _                ::
-- ::   _____   _____ _ __ | |_|  ___| | _____      __ ::
-- ::  / _ \ \ / / _ \ '_ \| __| |_  | |/ _ \ \ /\ / / ::
-- :: |  __/\ V /  __/ | | | |_|  _| | | (_) \ V  V /  ::
-- ::  \___| \_/ \___|_| |_|\__|_|   |_|\___/ \_/\_/   ::
-- ::                                                  ::
-- ::::::::::::::::::::::::::::::::::::::::::::::::::::::
-- ::::::::::::::::::::::::::::::::::::::::::::::::::::::

engine started ...
''')


# from kafka import KafkaProducer, KafkaConsumer
import requests
import redis
import time

# Pause execution for 5 seconds



# Kafka producer example
# producer = KafkaProducer(bootstrap_servers='localhost:9092')
# producer.send('my_topic', b'Hello, Kafka!')
# producer.flush()

# # Kafka consumer example
# consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092', group_id='my_group')
# for message in consumer:
#     print(message.value.decode())

# Requests example
# response = requests.get('https://google.com')
# print(response.status_code)
# print(response.json())

# Redis example
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set('my_key', 'my_value')
value = r.get('my_key')
print(value.decode())


time.sleep(2)
print('f')