FROM python:3

WORKDIR /kafka-producer

COPY . /kafka-producer

RUN pip install kafka-python

RUN pip install spidev

CMD ["python", "kafka-producer.py"]

