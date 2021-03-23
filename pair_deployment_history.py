#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import pdb;


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
arguments(smartContractAddress:
{is: "0xBCfCcbde45cE874adCB698cC183deBcF17952812"},
smartContractEvent: {is: "PairCreated"},
argument: {is: "pair"},
options: {desc: "block.height", limit: 1000000000}){
block {
height
}
argument {
name
}
reference {
address
}}
}}

"""
result = run_query(query)  # Execute the query
final_result = "{}".format(result)
writeFile = open('pairs.json', 'w')
writeFile.write(final_result)
writeFile.close()
