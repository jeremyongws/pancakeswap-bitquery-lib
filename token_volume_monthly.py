# dev's note - the query is extremely heavy and returns 504.

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

pools = ["""0x1b96b92314c44b159149f7e0303511fb2fc4774f"""]

# The GraphQL query
for pool in pools:
    # pdb.set_trace()
    query = """
{
ethereum(network: bsc){
dexTrades(options: {limit: 1000000, asc: "timeInterval.month"},
exchangeName: {is: "Pancake"}
baseCurrency: {is: "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"}){
transaction {
hash
}
smartContract{
address{
address
}
contractType
currency{
name
}}
tradeIndex
date {
date
}
timeInterval {
month(count: 1)
}
buyAmount
buyAmountInUsd: buyAmount(in: USD)
buyCurrency {
symbol
address
}
sellAmount
sellAmountInUsd: sellAmount(in: USD)
sellCurrency {
symbol
address
}
sellAmountInUsd: sellAmount(in: USD)
tradeAmount(in: USD)
transaction{
gasValue
gasPrice
gas
}}
}}
    """
    # pdb.set_trace()
    result = run_query(query)  # Execute the query
    final_result = "{}".format(result)
    print(final_result)
    writeFile = open('sample_pool_tvl.json', 'w')
    writeFile.write(final_result)
    writeFile.close()
