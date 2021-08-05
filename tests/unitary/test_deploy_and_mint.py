import pytest
import time
import numpy as np



    
def test_mint_article(test_deploy_contract, load_owner):

    return test_deploy_contract.mint(load_owner)
    

def test_NFT_props(test_deploy_contract, load_owner, N_articles):
	
    for i in range(N_articles):
        test_mint_article(test_deploy_contract, load_owner)
    
    tokenID = test_deploy_contract.viewTokenIDsforAddress(load_owner)

    
    assert len(tokenID) == N_articles


    return


def test_safeTransfer(test_deploy_contract, load_owner, load_account2, N_articles):
    	
    for i in range(N_articles):
        test_mint_article(test_deploy_contract, load_owner)
    
    tokenID = test_deploy_contract.viewTokenIDsforAddress(load_owner)
    transfer_idx = 3
    assert len(tokenID) == N_articles

    test_deploy_contract.transferFrom(load_owner,load_account2, transfer_idx, {'from':load_owner})  
    owners_NFTs = test_deploy_contract.viewTokenIDsforAddress(load_owner)
    account2_NFTs = test_deploy_contract.viewTokenIDsforAddress(load_account2)

    vals = np.arange(0,N_articles,1)
    vals = np.delete(vals,transfer_idx)
    vals = tuple(vals)
    

    assert owners_NFTs == vals
    assert account2_NFTs[0] == transfer_idx


    return


def test_citation():
    pass

def test_citation_burn():
    pass

def test

