#coding=utf-8
import os, json,datetime, pytz
from eth_utils import decode_hex
from utils import name_hash2
from settings import *

address = '0x5FfC014343cd971B7eb70732021E26C35B744cc4'
abi = json.load(open(os.path.join(BASE_DIR, 'abi/resolver.json')))
ens = web3.eth.contract(abi=abi, address=address)

def set_address(name, address, account, gas=100000, gas_price=''):
    name = name.lower()
    if not name.endswith('eth'):
        name = name + '.eth'
    name = decode_hex(name_hash2(name))
    if not gas_price:
        return ens.transact({'from':account, 'gas':gas}).setAddr(name, address)
    return ens.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).setAddr(name, address)
