
def get_user_profile(users, username):
    """Return a user's profile by username."""
    if username in users:
        return users[username]

    return None


def transfer_balance(accounts, source, destination, amount):
    """Transfer money between two accounts."""
    if source not in accounts or destination not in accounts:
        return False

    if accounts[source] < amount:
        return False

    accounts[source] -= amount
    accounts[destination] += amount
    return True


def main():
    accounts = {"alice": 100, "bob": 50}
    print(get_user_profile({"alice": {"role": "user"}}, "alice"))
    print(transfer_balance(accounts, "alice", "bob", -20))
    print(accounts)


if __name__ == "__main__":
    main()
