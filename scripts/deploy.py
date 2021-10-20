from brownie import FundMe
from scripts.utils import get_account, get_feed, get_verify

def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy(get_feed(),{"from":account}, publish_source=get_verify())
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()