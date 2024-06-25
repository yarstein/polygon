import json
from web3 import Web3
from polygon.settings import BASE_DIR

# наш endpoint для polygon из https://account.getblock.io/
polygon_RPC = "https://go.getblock.io/c7fbe9c35d6c429bb3d9c159d41f67d2"

# abi из приложенного файла
with open(BASE_DIR / 'erc20_abi.json', 'r') as abi_files:
    abi = json.load(abi_files)

# создаем объект Web3
w3 = Web3(Web3.HTTPProvider(polygon_RPC))

# ----------------------
# if w3.is_connected():
#     print("True")
# else:
#     print("False")
# ---------------------

# наш адрес преобразуем в checksum, без него ловим ошибку
token_address = Web3.to_checksum_address("0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0")
contract_instance = w3.eth.contract(address=token_address, abi=abi)


# Уровень А
def get_balance(address):
    """Query account balances"""
    checksum_address = Web3.to_checksum_address(address)
    balance = contract_instance.functions.balanceOf(checksum_address).call()
    return balance / (10 ** contract_instance.functions.decimals().call())


# Уровень B
def get_balance_batch(addresses):
    return [get_balance(adress) for adress in addresses]


# Уровень C, D - не смог реализовать, не понял как достать топ

# Уровень E
def get_token_info(address):
    checksum_address = Web3.to_checksum_address(address)
    contract_instance = w3.eth.contract(address=checksum_address, abi=abi)
    return {
        "symbol": contract_instance.functions.symbol().call(),
        "name": contract_instance.functions.name().call(),
        "totalSupply": contract_instance.functions.totalSupply().call() / (10 ** contract_instance.functions.decimals().call())
    }