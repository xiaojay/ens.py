#coding=utf-8
import os, json,datetime, pytz
from eth_utils import decode_hex
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8545'))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

address = '0x6090A6e47849629b7245Dfa1Ca21D94cd15878Ef'
abi = json.load(open(os.path.join(BASE_DIR, 'abi/registrar.json')))
registrar = web3.eth.contract(abi=abi, address=address)

def name_hash(name):
    return web3.sha3(web3.toHex(name))

def lookup(name):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    return registrar.call().entries(name)

def get_allowed_time2(name):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    ts = registrar.call().getAllowedTime(name)
    return datetime.datetime.fromtimestamp(ts, tz=pytz.UTC)

def get_allowed_time(name):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    return registrar.call().getAllowedTime(name)

def start_auction(name, account, gas=1000000, gas_price=''):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    if not gas_price:
        return registrar.transact({'from':account, 'gas':gas}).startAuction(name)
    return registrar.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).startAuction(name)

def bid(name, account, price, disguise_price, secret, gas=1000000, gas_price=''):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    secret = decode_hex(web3.sha3(web3.toHex(secret)))
    price = web3.toWei(price, 'ether')
    disguise_price = web3.toWei(disguise_price, 'ether')
    sb = registrar.call().shaBid(name, account, price, secret)
    if not gas_price:
        return registrar.transact({'from':account, 'gas':gas, 'value':disguise_price}).newBid(sb)
    return registrar.transact({'from':account, 'gas':gas, 'gasPrice':gas_price, 'value':disguise_price}).newBid(sb)

def unseal_bid(name, account, price, secret, gas=1000000, gas_price=''):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    secret = decode_hex(web3.sha3(web3.toHex(secret)))
    price = web3.toWei(price, 'ether')
    if not gas_price:
        return registrar.transact({'from':account, 'gas':gas}).unsealBid(name, price, secret)
    return registrar.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).unsealBid(name, price, secret)

def finalize(name, account, gas=1000000, gas_price=''):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    if not gas_price:
        return registrar.transact({'from':account, 'gas':gas}).finalizeAuction(name)
    return registrar.transact({'from':account, 'gas':gas, 'gasPrice':gas_price}).finalizeAuction(name)
    
