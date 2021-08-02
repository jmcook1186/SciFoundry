import pytest
import time
from brownie import (
    SciPaper,
    interface,
    accounts,
    network
)

    
def test_mint_article(test_deploy_contract, set_URI, load_owner):

    return test_deploy_contract.mint(load_owner, set_URI)
    

def test_NFT_props(test_deploy_contract, load_owner, set_URI, N_articles):
	
    for i in range(N_articles):
        test_mint_article(test_deploy_contract, set_URI, load_owner)
    tokenID = test_deploy_contract.viewTokenIDsforAddress(load_owner)
    URI = test_deploy_contract.viewURI(tokenID)
    
    assert tokenID == N_articles-1
    assert URI == set_URI
        

    return





