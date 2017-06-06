#coding=utf-8
import os, json,datetime, pytz
from eth_utils import decode_hex
from utils import name_hash2
from settings import *

address = '0x314159265dd8dbb310642f98f50c066173c1259b'
abi = json.load(open(os.path.join(BASE_DIR, 'abi/ens.json')))
ens = web3.eth.contract(abi=abi, address=address)

def get_owner(name):
    name = decode_hex(name_hash2(name))
    return ens.call().owner(name)
