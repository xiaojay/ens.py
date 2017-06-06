#coding=utf-8
from settings import *

def name_hash(name):
    return web3.sha3(web3.toHex(name))

def name_hash2(name):
    node = '0x0000000000000000000000000000000000000000000000000000000000000000'
    if name != '':
        labels = name.split('.')
        labels.reverse()
        for label in labels:
            node = web3.sha3(node + name_hash(label)[2:], encoding='hex')
    return node
