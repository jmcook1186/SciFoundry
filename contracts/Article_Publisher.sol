
pragma solidity ^0.6.6;

import '@openzeppelin/contracts/token/ERC721/ERC721.sol';

contract SciPaper is ERC721 {

  uint256 tokenID;
  uint256 tokenCount;
  address public owner;
  mapping(address => uint256) public addressTotokenID;
  mapping(uint256 => string) public tokenIDToURI;

  constructor() public ERC721('dPaper', 'PAP') {
    owner = msg.sender;
    tokenCount = 0;
  }

  function mint(address minter, string memory _tokenURI) external returns(uint256) {
    require(msg.sender == owner, 'only owner can mint');
    tokenID = tokenCount;
    addressTotokenID[msg.sender] = tokenID;
    _safeMint(minter, tokenID);
    _setTokenURI(tokenID, _tokenURI);
    tokenIDToURI[tokenID] = _tokenURI;

    tokenCount+=1;

  }
   

function viewURI(uint256 tokenID) public view returns(string memory) {

    return tokenIDToURI[tokenID];
}

function viewTokenIDsforAddress(address user) public view returns(uint256){

    return addressTotokenID[user];
}


}