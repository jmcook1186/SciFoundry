
pragma solidity ^0.6.6;

import '@openzeppelin/contracts/token/ERC721/ERC721.sol';

contract SciFactory is ERC721 {

  uint256 tokenID;
  uint256 tokenCount;
  address public owner;
  mapping(address => uint256[]) addressTotokenID;
  mapping(uint256 => string) public tokenIDToURI;

  constructor() public ERC721('dArticle', 'dART') {
    owner = msg.sender;
    tokenCount = 0;
  }


  /**
  @dev
  uses tokenID to map NFT to its metadata
  
  BaseURI is used to navigate to URI of directory containing each .json file
  tokenURI is then the base URI + the token ID and .json suffix (i.e. specific file)

  metadata number and tokenID must remain in sync for correct image/metadata to
  associate with a specific minted NFT
  
  */
  function setURI () internal {


    string memory baseURI = "https://github.com/jmcook1186/jmcook1186.github.io/blob/main/Data/NFT_Metadata/NFT_metadata_";
    string memory suffix = ".json";
    string memory tokenURI = string(abi.encodePacked(baseURI, tokenID.toString(),suffix));
    _setTokenURI(tokenID, tokenURI);
    tokenIDToURI[tokenID] = tokenURI;

  }


  /** 
  @dev
  Mints NFT
  must be called by the contract owner, else fail
  pushes token ID to array mapped to minter address
  calls internal set_URI function to associated NFT to metadata
  increments tokenCount by 1
  
  */
  function mint(address minter) external onlyOwner returns(uint256) {

    tokenID = tokenCount;
    addressTotokenID[msg.sender].push(tokenID);
    _safeMint(minter, tokenID);
    setURI();
    tokenCount+=1;
    
    return (tokenID);
  }
  

  /**
  @dev
  public view function returns URI for specific token

  */

  function viewURI(uint256 _tokenID) public view returns(string memory) {

      return tokenIDToURI[_tokenID];
  
  }



  /**
  @dev
  public view function returns array of tokenIDs 
  owned by given address

  */
  function viewTokenIDsforAddress(address user) public view returns(uint256[] memory){

      uint256 N_IDs = addressTotokenID[user].length;
      uint256[] memory IDs  = addressTotokenID[user];
      
      return IDs;
  }

  
  /**
   @dev
   using simple delete operation leaves behind a zero that is easily 
   misinterpreted as tokenID 0. Therefore, move the doomed element
   to the end of the array then shorten the array to erase completely.
   Do this by whipping up small internal function "delete_element", 
   then call it from inside safeTranferFrom().
  */
  function delete_element(uint idx, uint256[] storage _array) internal returns(uint256[] storage){
    
    if(idx >= _array.length){return _array;}

    for (uint i = idx; i<_array.length-1; i++){
      _array[i] = _array[i+1];
    }

    //delete _array[_array.length-1];
    _array.pop();

    return _array;

  }



  /**
  @dev
  overrides safeTransferFrom in ERC721 standard to maintain synchronicity with
  address=>tokenID mapping in addressTotokenID.
  
  */
  function safeTransferFrom(address from, address to, uint256 _tokenID, bytes memory _data) public override{
    require(_isApprovedOrOwner(_msgSender(), _tokenID), "ERC721: transfer caller is not owner nor approved");
    _safeTransfer(from, to, _tokenID, _data);


    addressTotokenID[from] = delete_element(_tokenID, addressTotokenID[from]);

    addressTotokenID[to].push(_tokenID);
    
    }


  /**
  @dev
  overrides ERC721 transferFrom with call to safeTransferFrom()
  */
  function transferFrom(address from, address to, uint256 _tokenID) public override {
    
    safeTransferFrom(from, to, _tokenID);

    }


  modifier onlyOwner() {
    require(owner == msg.sender);
    _;
  }

}