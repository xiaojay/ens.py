#coding=utf-8
import os, json,datetime, pytz
from eth_utils import decode_hex
from utils import name_hash2, get_name_node
from settings import *

address = '0x314159265dd8dbb310642f98f50c066173c1259b'
abi = json.load(open(os.path.join(BASE_DIR, 'abi/ens.json')))
ens = web3.eth.contract(abi=abi, address=address)

def get_owner(name):
    return ens.call().owner(get_name_node(name))

def get_resolver(name):
    return ens.call().resolver(get_name_node(name))

def get_ttl(name):
    return ens.call().ttl(get_name_node(name))

def set_resolver(name, resolver, account, gas=100000, gas_price=''):
    name = get_name_node(name)
    if not gas_price:
        return ens.transact({'from':account, 'gas':gas}).setResolver(name, resolver)
    return ens.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).setResolver(name, resolver)

def set_owner(name, address, account, gas=100000, gas_price=''):
    name = get_name_node(name)
    if not gas_price:
        return ens.transact({'from':account, 'gas':gas}).setOwner(name, address)
    return ens.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).setOwner(name, address)
