#coding=utf-8
import os, json,datetime
from eth_utils import decode_hex
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8545'))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

address = '0x6090A6e47849629b7245Dfa1Ca21D94cd15878Ef'
abi = json.load(open(os.path.join(BASE_DIR, 'abi/registrar.json')))
registrar = web3.eth.contract(abi=abi, address=address)

def lookup(name):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    return registrar.call().entries(name)

def get_allowed_time(name):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    ts = registrar.call().getAllowedTime(name)
    return datetime.datetime.fromtimestamp(ts)

def start_auction(name, account, gas=1000000):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    return registrar.transact({'from':account, 'gas':gas}).startAuction(name)

def bid(name, account, price, disguise_price, secret, gas=1000000):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    secret = decode_hex(web3.sha3(web3.toHex(secret)))
    price = web3.toWei(price, 'ether')
    disguise_price = web3.toWei(disguise_price, 'ether')
    sb = registrar.call().shaBid(name, account, price, secret)
    return registrar.transact({'from':account, 'gas':gas, 'value':disguise_price}).newBid(sb)

def unseal_bid(name, account, price, sercrect, gas=1000000):
    name = decode_hex(web3.sha3(web3.toHex(name)))
    secret = decode_hex(web3.sha3(web3.toHex(secret)))
    price = web3.toWei(price, 'ether')
    return registrar.transact({'from':account, 'gas':gas}).unsealBid(name, price, secret)
