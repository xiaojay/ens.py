#coding=utf-8
import os
from web3 import Web3, KeepAliveRPCProvider, IPCProvider
web3 = Web3(KeepAliveRPCProvider(host='127.0.0.1', port='8545'))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
