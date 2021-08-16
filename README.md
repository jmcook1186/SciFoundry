# Sci Foundry

SciFoundry is a proof of concept minimum viable product for decentralised science publishing using Ethereum and NFTs.
Right now this project is deployable locally (Ganache) or on Rinkeby.

Initial aim is to develop nearly-free, transparent, decentralised science article publishing system that tracks 
article/user metrics by minting dynamic NFTs representing individual science articles. 

Current functionality:
	- User writes article and mints it as NFT using SciFoundry contract
	- NFT visible on OpenSea with image, properties and link to full m/s and datasets
	- NFT tracks citation metrics which are viewable on OpenSea
	- Other users can submit a manuscript review as numeric score and link to text comments
	- NFT tracks review scores and presents their mean as a "trust score" for the article on OpenSea

# TODOs

1. find way to share ownership of NFT between multiple authors
2. build front end that queries citations and trust score from contract view func and updates NFT metadata
3. Consider a payment layer, which could be the owner of the SciFoundry contract (ie. mint only ater payment)
4. Payment layer should collect incoming funds and periodically park in DeFi lending pool (Aave?)
5. NFT URI should link to IPFS not https
6. Build out tests


# How to Use

## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already.

2. If you want to be able to deploy to testnets, do the following.
	Set your WEB3_INFURA_PROJECT_ID and PRIVATE_KEY environment variables
	You can get a WEB3_INFURA_PROJECT_ID by getting a free trial of Infura. At the moment, it does need to be infura with brownie. 
	If you get lost, follow the instructions at   https://ethereumico.io/knowledge-base/infura-api-key-guide/. 
	You can find your PRIVATE_KEY from your ethereum wallet like metamask.

    You'll also need testnet ETH. You can get Rinkeby ETH by tweetign your wallet address then providing the tweet url to the following faucet:
    https://faucet.rinkeby.io/ 

    You can add your environment variables to a .env file. You can use the .env_example in this repo 
    as a template, just fill in the values and rename it to '.env'. 

    Here is what your .env should look like:

    ```bash
    export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
    export PRIVATE_KEY=<PRIVATE_KEY>
    ```
   
3. Create brownie account(s) following instructions here:
       https://eth-brownie.readthedocs.io/en/stable/account-management.html

4. Import the brownie account to MetaMask using their private key(s)


5. Open the Brownie console. Starting the console launches a fresh [Ganache](https://www.trufflesuite.com/ganache) instance in the background.

    ```bash
    $ brownie console
    Brownie v1.9.0 - Python development framework for Ethereum

    ReactMixProject is the active project.
    Launching 'ganache-cli'...
    Brownie environment is ready.
    ```

    Alternatively, to run on Rinkeby, set the network flag to kovan

    ```bash
    $ brownie console --network Rinkeby
    Brownie v1.14.6 - Python development framework for Ethereum

    ReactMixProject is the active project.
    Brownie environment is ready.
    ```

6. Run the [deployment script](scripts/deploy.py) to deploy the project's smart contracts. Alternatively deploy interactively in the console

```
# on the Rinkeby network (delete network flag for local deploy)
brownie console --network Rinkeby

account = accounts.load('main')
Foundry = SciFoundry.deploy({'from': account})

```

7. Mint an article NFT

Minting an NFT requires that the metadata file has alrady been saved to the location pointed to by the token URI. In future, this file
will be created via the front-end at the same time as minting. The first NFT minted cannot cite any others because no others exist, so
pass an empty array. Later mints can cite existing ones by passing token_IDs.

```
# Foundry.mint(address minter, uint256[] _citedIDs, {'from': Account})

Foundry.mint(account, [], {'from':account})

```

To check that a token has been minted successfully, call the totalSupply() function and check it has incremented by 1.
Check the token's metrics using the public view functions passing the tokenID.

```
# how many tokens have been minted?
Foundry.totalSupply() 

# how many sitations does token 0 have?
Foundry.citationCounter(0)

# What is the trust score for token 0?
Foundry.trustScore(0)

# How many times has token 0 been reviewed?
Foundry.nReviews(0)

```


8. Review Articles
To conduct a peer-review on an article, use the SciFoundry contract's reviewArticle functio. The arguments to pass are the tokenID
(i.e. which article to review), a numeric score (/100) and a link to a set of review comments (ideally this will point to a pinned IPFS file).
The contract will automatically aggregate this scre with previous reviews an update the NFT's trust score. 

```
# give token 0 a rveiew score of 50% and link to comments
Foundry.reviewArticle(0, 50, "https://some_url", {'from': account})

```

To see previous reviews of a particular article, use the reviewLinks function passing the tokenID and the index for the specific comments to view.
The link to the text comments is returned.

```
# see text comments for the 3rd review (indexed from 0: idx = 2) of NFT 1:
Foundry.reviewinks(1, 2)

```

To query the external URL link for the article, pass the tokenID to tokenIDtoURI

```
# what is the full manuscript link for tokenID 0?
Foundry.tokenIDToURI(0)

```

9. View a user's NFTs

To see which token_IDs are owned by a specific user, query viewTokenIDsforAddress passing the user's address

```

Foundry.viewTokenIDsforAddress('0x...')

```

10. View a user's overall score

A user's score needs to be periodically recalculated by explicitly calling the calculateUserScore function passing
the user's address. This function should probably be made internal and automatically executed in the reviewing function
but I have not decided on a sensible place for it yet. The function iterates through the NFTs they own and returns 
the arithmetic mean of their trust scores, saving the result to a mapping. This mapping is then queried via the public view function viewuserScore.

```
# recalculate user score
Foundry.calculateUserScore('0x...')

view user score
FoundryviewUserScore('0x...')

```

## OpenSea

A version of this contract is deployed on the Rinkeby network and an example article NFT is viewable on OpenSea (https://testnets.opensea.io/assets/0xE77D0f2b83c558DDb10eD98fF100615Cca2FaF3d/0/). For the example I just chose one of my previously published articles to deploy. To ensure the 
displayed metrics are up to date, run the Python script update_metrics.py. This script queries the Rinkeby blockchain and retrieves the latest data 
for a specific NFT and updates its metadata file. This should then automatically update on the NFT's OpenSea listing.

## Authors

Joseph Cook

# Status
code is under development and is not covered by any warranty neither explicit nor implied. This code has not been audited.

