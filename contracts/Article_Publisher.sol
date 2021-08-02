
pragma solidity ^0.6.6;

import '@openzeppelin/contracts/token/ERC721/ERC721.sol';

contract SciFactory is ERC721 {

  uint256 tokenID;
  uint256 tokenCount;
  address public owner;
  mapping(address => uint256) public addressTotokenID;
  mapping(uint256 => string) public tokenIDToURI;

  constructor() public ERC721('dPaper', 'PAP') {
    owner = msg.sender;
    tokenCount = 0;
  }

  function setURI () internal {
    string memory baseURI = "https://github.com/jmcook1186/jmcook1186.github.io/blob/main/Data/NFT_Metadata/NFT_metadata_";
    string memory suffix = ".json";
    string memory tokenURI = string(abi.encodePacked(baseURI, tokenID.toString(),suffix));
    _setTokenURI(tokenID, tokenURI);
    tokenIDToURI[tokenID] = tokenURI;

  }

  function mint(address minter) external returns(uint256) {
    require(msg.sender == owner, 'only owner can mint');
    tokenID = tokenCount;
    addressTotokenID[msg.sender] = tokenID;
    _safeMint(minter, tokenID);
    setURI();
    tokenCount+=1;
    
    return (tokenID);
  }
  


  function viewURI(uint256 tokenID) public view returns(string memory) {

      return tokenIDToURI[tokenID];
  }

  function viewTokenIDsforAddress(address user) public view returns(uint256){

      return addressTotokenID[user];
  }


}