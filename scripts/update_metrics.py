import os
import json
from github import Github
from git import Repo
from brownie import (
     Contract,
     accounts,
     network,
)


def load_owner():
    owner = accounts.load('main')
    return owner

def get_contract():

    netw = network.show_active()
    if netw=='rinkeby':
        foundry = Contract('0xc4dAB6BEbfe831b77dCA495733b5BBb986a212C9')
    else:
        raise ValueError("try Rinkeby network")
    
    return foundry


def update_metadata(foundry, baseURI, token_ID):

    changes = 0
    localURI = '/Data/NFT_Metadata/NFT_metadata_{}.json'.format(token_ID)

    with open(str(baseURI+localURI)) as json_in_file:

        data = json.load(json_in_file)
        
    citations_api = data['attributes'][5]['value']
    trust_score_api = data['attributes'][6]['value']
    nReviews_api = data['attributes'][7]['value']

    citations_chain = foundry.citationCounter(token_ID)
    trust_score_chain = foundry.trustScore(token_ID)
    nReviews_chain = foundry.nReviews(token_ID)
    
    if citations_api != citations_chain:
        data['attributes'][5]['value'] = citations_chain
        changes+=1
    if trust_score_api != trust_score_chain:
        data['attributes'][6]['value']= trust_score_chain
        changes+=1
    if nReviews_api != nReviews_chain:
        data['attributes'][7]['value'] = nReviews_chain
        changes+=1
    
    with open(str(baseURI+localURI), 'w') as json_out_file:

        json.dump(data, json_out_file, indent = 4)


    return changes ,localURI


def commit_and_push(localURI, commit_mesage):
    """
    requires git personal access token to be provided in .env file
    or set as environment variable in shell
    """
    print("hello")
    current_path = os.getcwd()
    path_to_repo = '/home/joe/Code/jmcook1186.github.io'
    os.chdir(path_to_repo)
    
    g= Github(os.environ["GIT_TOKEN"])
    repo = Repo(path_to_repo)
    
    repo.index.add(localURI)
    repo.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()

    os.chdir(current_path)

    return

# load path to metadata file
token_ID = 0 #which NFT are we interested in?
localURI = '/home/joe/Code/jmcook1186.github.io/Data/NFT_Metadata/NFT_metadata_{}.json'.format(token_ID)
baseURI = '/home/joe/Code/jmcook1186.github.io' # where is the local git repo?
commit_message = "update NFT metadata due to change in on-chain metrics"

# function calls
owner= load_owner()
foundry = get_contract()
changes = update_metadata(foundry, baseURI, token_ID)

if changes>0: #only if the file has changed
    commit_and_push(localURI, commit_message)


