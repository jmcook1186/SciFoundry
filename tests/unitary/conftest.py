import pytest

from brownie import (
    SciFactory,
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

@pytest.fixture(scope='module')
def load_account2():
    account2 = accounts.load('account2')
    return account2

@pytest.fixture
def test_deploy_contract(checkNetwork, load_owner):
    
    if checkNetwork == 'kovan':
        return Contract(deployed_address)
    
    elif checkNetwork == 'development':
    	return SciFactory.deploy({'from':load_owner})
    	
@pytest.fixture
def N_articles():
    return 5
