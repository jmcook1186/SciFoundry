# Sci Foundry
SciFoundry is a proof of concept minimum viable product for decentralised science publishing using Ethereum and NFTs.
Initial aim is to develop nearly-free, transparent, decentralised science article publishing system that tracks article/user metrics by minting dynamic NFTs.

Current functionality:
	- user writes article and mints it as NFT
	- NFT visible on OpenSea with image and properties
	- NFT tracks citation metrics
	- full paper downloadable to anyone by visiting the external_url in NFT metadata

# TODOs

1. find way to share ownership of NFT between multiple accounts
2. enable submission of reviews and calculation of article-level trust score
3. build front end that queries citations and trust score from contract view func and updates NFT metadata
4. build proper tests
5. NFT URI should link to IPFS not https
6. consider contract owner being secndary contract that mints on payment of DAI
7. deposit accumulated DAI into aave lending pool to generate profit


# Status
code is under development and is not covered by any warranty neither explicit nor implied. This code has not been audited.

