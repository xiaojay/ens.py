#coding=utf-8
import os, json,datetime, pytz
from eth_utils import decode_hex
from utils import name_hash2, get_name_node
from settings import *

address = '0x5FfC014343cd971B7eb70732021E26C35B744cc4'
abi = json.load(open(os.path.join(BASE_DIR, 'abi/resolver.json')))
resolver = web3.eth.contract(abi=abi, address=address)

def set_address(name, address, account, gas=100000, gas_price=''):
    name = get_name_node(name)
    if not gas_price:
        return resolver.transact({'from':account, 'gas':gas}).setAddr(name, address)
    return resolver.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).setAddr(name, address)

def get_address(name):
    return resolver.call().addr(get_name_node(name))

def set_content(name, address, account, gas=100000, gas_price=''):
    name = get_name_node(name)
    if not gas_price:
        return resolver.transact({'from':account, 'gas':gas}).setContent(name, content)
    return resolver.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).setContent(name, content)

def get_content(name):
    return resolver.call().content(get_name_node(name))

def set_name(name, name2, account, gas=100000, gas_price=''):
    name = get_name_node(name)
    if not gas_price:
        return resolver.transact({'from':account, 'gas':gas}).setName(name, name2)
    return resolver.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).setName(name, name2)

def get_name(name):
    return resolver.call().name(get_name_node(name))

def set_text(name, key, value, account, gas=100000, gas_price=''):
    name = get_name_node(name)
    if not gas_price:
        return resolver.transact({'from':account, 'gas':gas}).setText(name, key, value)
    return resolver.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).setText(name, key, value)

def get_text(name, key):
    return resolver.call().text(get_name_node(name), key)
