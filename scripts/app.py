import json
import os
from brownie import accounts, network, SciFactory
from web3 import Web3

def main():
    owner = accounts.load('main')
    public_key = "0xa0F57bd9E5F156BD60Ff214abA29c4cAF6d2C386"
    private_key = os.environ['PRIVATE_KEY']

    if network.show_active() == 'development':
        web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        contract = SciFactory.deploy({'from':owner})

    else: raise ValueError("not yet deploying to public blockchains")

    nft = contract.mint(owner,{'from':owner})
    print(contract.totalSupply())
