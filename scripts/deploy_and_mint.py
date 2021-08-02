from brownie import SciPaper, network, accounts, config



def deploy(contract_owner):
    
    print("ACTIVE NETWORK: {}".format(network.show_active()))
    
    ArticleFactory = SciPaper.deploy({'from':contract_owner})
    
    contract_address = ArticleFactory.address
    print("Article contract successfully deployed to {}".format(contract_address))
    
    return ArticleFactory
    

def mint_article(ArticleFactory, URI, author):
        
    ArticleFactory.mint(author, URI)

    return
    

def check_NFT_props(ArticleFactory, author):

    tokenID = ArticleFactory.viewTokenIDsforAddress(author)
    URI = ArticleFactory.viewURI(tokenID)
    
    print("The request came from {}".format(author))
    print("This address owns NFT number {}".format(tokenID))
    print("That NFT has the following URI: {}".format(URI))
    

    return


def main():

    owner = accounts.load("main")
    URI = "https://raw.githubusercontent.com/jmcook1186/jmcook1186.github.io/main/Data/NFT_metadata.json"

    ArticleFactory = deploy(owner)
    mint_article(ArticleFactory, URI, owner)
    check_NFT_props(ArticleFactory, owner)
    
    return
