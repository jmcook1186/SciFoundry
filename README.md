# Sci Foundry
SciFounry is a proof of concept minimum viable product for decentralised science publishing using Ethereum and NFTs.
Initial aim is to develop nearly-free, transparent, decentralised science article publishing system that tracks article/user metrics by minting dynamic NFTs.

Current functionality:
	user writes article and mints it as NFT
	NFT visible on OpenSea with image and properties
	NFT tracks citation metrics
	full paper downloadable to anyone by visiting the external_url in NFT metadata

# TODOs

1. find way to share ownership of NFT between multiple accounts
2. build front end that queries citations from contract view func and updates NFT metadata
3. build proper tests
4. NFT URI should link to IPFS not https
5. consider contract owner being secndary contract that mints on payment of DAI
6. deposit accumulated DAI into aave lending pool to generate profit


# Status
code is under development and is not covered by any warranty neither explicit nor implied. This code has not been audited.

