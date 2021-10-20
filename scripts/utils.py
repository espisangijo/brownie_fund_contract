from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 20000000000
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS= ["development", "ganache-local"]

def get_account():
    # using random account by ganache-cli
    # account = accounts[0]

    # $ brownie accounts new demo
    # $ enter private key
    # $ encrypt with password
    # > account = accounts.add("demo")

    # using environment variable/file
    # account = accounts.add(os.getenv("PRIVATE_KEY"))

    # does the same thing as above, but with config.yml instead of .env
    # account = accounts.add(config["wallets"]["from_key"])
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS :
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def get_feed():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        # mock
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE,"ether"), {"from":get_account()})
        
        price_feed_address = MockV3Aggregator[-1].address
        return price_feed_address

def get_verify():
    return config["networks"][network.show_active()].get("verify")

def deploy_mock():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(18, Web3.toWei(2000,"ether"), {"from":get_account()})
        