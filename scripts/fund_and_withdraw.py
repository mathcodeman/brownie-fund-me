from brownie import FundMe
from scripts.helper import get_account

fund_me = FundMe[-1]
account = get_account()


def fund():
    # Retrieve the last contract that deployed to the blockchain
    entrance_fee = fund_me.getEntranceFee() * 10000000000
    print(entrance_fee)
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me.withdraw({"from": account})


def main():
    withdraw()
    print(f"{fund_me.address} has been transferred to your account")
