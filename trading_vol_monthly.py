#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pdb


def run_query(query):  # A simple function to use requests.post to make the API call.
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))


# The GraphQL query

query = """

{
ethereum(network: bsc){
dexTrades(options: {limit: 1000, asc: "timeInterval.month"},
date: {since:"2020-01-01"}
exchangeName:{is:"Pancake"}){
timeInterval {
month(count: 1)
}
count
tradeAmount(in: USD)
}
}}

"""
result = run_query(query)  # Execute the query
# pdb.set_trace()
print("Result - {}".format(result))
