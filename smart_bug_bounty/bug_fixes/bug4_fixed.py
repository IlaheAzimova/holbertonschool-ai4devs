
def transfer_balance(accounts, source, destination, amount):
    """Transfer a positive amount between existing accounts."""
    if source not in accounts or destination not in accounts:
        return False
    if amount <= 0:
        return False
    if accounts[source] < amount:
        return False

    accounts[source] -= amount
    accounts[destination] += amount
    return True


def main():
    accounts = {"alice": 100, "bob": 50}
    assert transfer_balance(accounts, "alice", "bob", 20)
    assert accounts == {"alice": 80, "bob": 70}

    assert not transfer_balance(accounts, "alice", "bob", -10)
    assert not transfer_balance(accounts, "alice", "bob", 0)
    assert accounts == {"alice": 80, "bob": 70}
    print("bug4_fixed.py: All 4 tests passed")


if __name__ == "__main__":
    main()
