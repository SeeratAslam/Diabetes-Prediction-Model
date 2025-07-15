# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:06:08 2025

@author: Mughal PC
"""

import json
import requests

url = 'http://127.0.0.1:8000/diabetes_prediction'

input_data_for_model = {
    
    'Pregnancies' : 1,
    'Glucose' : 85,
    'BloodPressure' : 66,
    'SkinThickness' : 29,
    'Insulin' : 0,
    'BMI' : 26.6,
    'DiabetesPedigreeFunction' : 0.351,
    'Age' : 31
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)