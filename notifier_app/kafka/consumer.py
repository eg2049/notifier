# -*- coding: utf-8 -*-

"""
Use Python 3.10.0

Kafka consumer
"""

import json

from kafka import KafkaAdminClient, KafkaConsumer
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

from config.config import KAFKA_BROKERS


def json_deserializer(event: bytes) -> dict:
    """Десериализатор получаемых событий kafka

    Args:
        event (bytes): payload события kafka, который будет десериализовываться 
            (атрибут value у kafka.consumer.fetcher.ConsumerRecord), 
            ожидается что в value будет сериализованный json, передаваемый как поток байт

    Returns:
        dict: десериализованный value
    """

    return json.loads(s=event)


def topic_exists_checker(topic: str) -> bool:
    """Проверка существования топика

    Args:
        topic (str): название топика

    Returns:
        bool: существует ли топик
    """

    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_BROKERS
    )

    topic_list = admin_client.list_topics()

    return topic in topic_list


def topic_creator(name: str, num_partitions: int = 1, replication_factor: int = 1) -> None:
    """Создание нового топика

    Args:
        name (str): название топика
        num_partitions (int, optional): количество партиций топика. Defaults to 1.
        replication_factor (int, optional): количество реплик топика. Defaults to 1.
    """

    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_BROKERS
    )

    new_topic = NewTopic(name=name, num_partitions=num_partitions,
                         replication_factor=replication_factor)

    try:
        admin_client.create_topics(
            new_topics=[
                new_topic
            ]
        )

    except TopicAlreadyExistsError:
        pass


def consumer_creator(topic: str, consumer_group_id: str, auto_offset_reset: str = 'earliest') -> KafkaConsumer:
    """Создание инстанса KafkaConsumer

    Args:
        topic (str): название топика
        consumer_group_id (str): название consumer группы
        auto_offset_reset (str, optional): начиная с какого события необходимо читать топик. Defaults to 'earliest'.

    Returns:
        KafkaConsumer: инстанс KafkaConsumer
    """

    consumer = KafkaConsumer(

        # топик из которого нужно читать события
        topic,

        # адреса брокеров
        bootstrap_servers=KAFKA_BROKERS,

        # с какого события начинать читать
        auto_offset_reset=auto_offset_reset,

        # к какой consumer group относится consumer
        # 1 topic & 2 partition-а и 1 consumer в ОДНОЙ consumer group - consumer будет получать события из ОБОИХ partition-ов
        # 1 topic & 1 partition и 2 consumer-а в ОДНОЙ consumer group - события будет получать ТОЛЬКО ОДИН consumer
        # 1 topic & 1 partition и 2 consumer-а в РАЗНЫХ consumer group - события будут получать ОБА consumer-а
        # 1 topic & 2 partition-а и 2 consumer-а в ОДНОЙ consumer group - КАЖДЫЙ consumer будет получать события ТОЛЬКО ИЗ СВОЕГО partition-а
        group_id=consumer_group_id,

        # десериализатор для событий
        value_deserializer=json_deserializer
    )

    return consumer


if __name__ == '__main__':
    pass
