from web3 import Web3

#network endpoints
mainnet = Web3(Web3.HTTPProvider("https://eth-mainnet.alchemyapi.io/v2/X"))
rinkeby = Web3(Web3.HTTPProvider("https://eth-rinkeby.alchemyapi.io/v2/X"))
ropsten = Web3(Web3.HTTPProvider("https://eth-ropsten.alchemyapi.io/v2/X"))

#getting the current block number of each chain
mainnet_block = mainnet.eth.blockNumber 
rinkeby_block = rinkeby.eth.blockNumber
ropsten_block = ropsten.eth.blockNumber

#getting the balance of the account at the current block. If we wanted a different block the second parameter can be used to select what block we want to query the account balance. 
mainnet_balance = mainnet.eth.get_balance('0xB07626Bc2fF18d680ec886c3109e9BF6ee05E6b7')
rinkeby_balance = rinkeby.eth.get_balance('0xB07626Bc2fF18d680ec886c3109e9BF6ee05E6b7')
ropsten_balance = ropsten.eth.get_balance('0xB07626Bc2fF18d680ec886c3109e9BF6ee05E6b7')

#print results 
print("The balance of the account on Mainnet is", mainnet_balance, "wei queried at block number", mainnet_block)
print("The balance of the account on Rinkeby is", rinkeby_balance, "wei queried at block number", rinkeby_block)
print("The balance of the account on Rinkeby is", ropsten_balance, "wei queried at block number", ropsten_block)

# The balance of the account on Mainnet is 939467857647043 wei queried at block number 14573329
# The balance of the account on Rinkeby is 0 wei queried at block number 10493711
# The balance of the account on Rinkeby is 2998595976150017072 wei queried at block number 12189341