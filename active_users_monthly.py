#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pdb;
import csv


def run_query(query):  # A simple function to use requests.post to make the API call.
    request = requests.post('https://graphql.bitquery.io/',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                        query))

pools = ["""0x1b96b92314c44b159149f7e0303511fb2fc4774f"""]

# The GraphQL query
for pool in pools:
    # pdb.set_trace()
    query = """
{
ethereum(network: bsc){
dexTrades(options: {limit: 1000, asc: "timeInterval.month"},
exchangeName:{is:"Pancake"}){
timeInterval {
month(count: 1)
}
count: count
callers: count(uniq: senders)
totalGas: gasValue
}
}}


    """
    # pdb.set_trace()
    result = run_query(query)  # Execute the query
    final_result = "{}".format(result)
    print(final_result)
    writeFile = open('active_users.json', 'w')
    writeFile.write(final_result)
    writeFile.close()
