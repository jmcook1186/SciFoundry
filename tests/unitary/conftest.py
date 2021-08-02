import pytest

from brownie import (
    SciPaper,
    Contract,
    accounts,
    network,
)

@pytest.fixture
def checkNetwork():
    return network.show_active()

@pytest.fixture(scope='module')
def load_owner():
    owner = accounts.load('main')
    return owner

@pytest.fixture
def set_URI():
    return "https://raw.githubusercontent.com/jmcook1186/jmcook1186.github.io/main/Data/NFT_metadata.json"

@pytest.fixture
def test_deploy_contract(checkNetwork, load_owner):
    
    if checkNetwork == 'kovan':
        return Contract(deployed_address)
    
    elif checkNetwork == 'development':
    	return SciFactory.deploy({'from':load_owner})
    	
@pytest.fixture
def N_articles():
    return 5
