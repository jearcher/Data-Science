#!/usr/bin/env python
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"

# Add at least 1 metadata to each of the following:

@app.route("/purchase_a_sword")
def purchase_a_sword():
    purchase_sword_event = {'event_type': 'purchase_sword', 
            'sword_type': 'one_handed'} # Added by JA
    log_to_kafka('events', purchase_sword_event)
    return "Sword Purchased!\n"

#####################
#### Added by JA ####
#####################

@app.route("/buy_a_sword")
def buy_a_sword():
    buy_sword_event = {'event_type': 'buy_sword',
            'sword_condition': 'rustyAF'}
    log_to_kafka('events', buy_sword_event)
    return "Sword Bought!\n"

@app.route("/join_guild")
def join_sword():
    join_guild_event = {'event_type': 'join_guild',
            'guild_name': 'TheHorde'}
    log_to_kafka('events', join_guild_event)
    return "Guild Joined!\n"

