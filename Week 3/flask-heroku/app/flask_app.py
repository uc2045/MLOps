# import modules
from flask import Flask, jsonify, request
from app.bmivalue import bmi_value
import json

# instantiate flask object
#app = Flask()
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def get_input():
    '''
    A function to get requests using flask, evaluate and return result.
    '''

    packet = request.get_json(force=True)
    weight = packet['weight']
    height = packet['height']

    bmi = bmi_value(weight, height)

    #return jsonify(packet, bmi)
    return {"packet": packet, "bmi": bmi}
