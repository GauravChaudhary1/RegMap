# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:02:42 2021

@author: Gaurav
"""

from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import os
from sentence_transformers import SentenceTransformer, util
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


app = Flask(__name__)
api = Api(app)

CORS(app)

cf_port = os.getenv("PORT")

def read_corpus():
    corpus = ['Adjustments to inventory prices and costs values relate to valid price changes.',
          'Journal entries are independently reviewed, validated, authorized, and properly recorded in the appropriate accounting period.',
          'Journal entries recorded during the period-end accounting close process are reviewed by someone independent of the journal entry preparation and recording process for significant and unusual activity.',
          'Only valid changes are made to the item master file.',
          'Accounts Receivable reflect the existing business circumstances and economic conditions in accordance with accounting policies being used.',
          'Only valid orders are input and processed.',
          'Fixed asset register and/or master file data remains pertinent.',
          'Ensure employees are paid are least minimum wage in compliance with the Fair Labor Standard Act.',
          'Ensure federal taxes are withheld in accordance with IRC guidelines.'
          ]
    return corpus
    
    
def execute_query(query):
    corpus = read_corpus()
    embedder = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    cos_scores = cos_scores.cpu()

    #We use np.argpartition, to only partially sort the top 5 results
    top_results = np.argpartition(-cos_scores, range(5))[0:5]
    retList = []
    for idx in top_results[0:5]:
        dict = {}
        dict['control'] = corpus[idx].strip()
        dict['score'] =round(( cos_scores[idx].item() * 100 ),2)
        dict['mapped'] = 'decline'
        retList.append(dict)
    
    
    return retList
        

@app.route("/")
def hello():
    x = request.args
    y = x["qStr"]
    result = execute_query(y)
    results_test1 = dumps(result) 
    return jsonify(results_test1) 

class Employees(Resource):
    def get(self):
        x = request.args
        y = x["_limit"]
        return {'employees': [{'id':1, 'name':'Balram' ,'data': y},{'id':2, 'name':'Tom'}]} 

class Employees_Name(Resource):
    def get(self, employee_id):
        #result = {'data': {'id':1, 'name':'Balram', 'emp':employee_id}}
        result = execute_query('Only valid orders are taken into consideration')
        return jsonify(result)       


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
  

if __name__ == '__main__':
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port),debug=True)
