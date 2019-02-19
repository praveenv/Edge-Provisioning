from kafka import KafkaConsumer

consumer = KafkaConsumer('test', # topic to subscribe to - TODO : Include multiple topics
        bootstrap_servers=['128.195.53.171:9092'], # server to connect to
        auto_offset_reset='earliest', # if consumer goes down reload from oldest 
        enable_auto_commit=True,
        group_id='analog_sensors'
        )
