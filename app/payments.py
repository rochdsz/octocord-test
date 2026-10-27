import urllib2  # VIOLATION: Deprecated package

# VIOLATION: Hardcoded plaintext dummy secret
PAYMENT_SECRET_TOKEN = "dummy_secret_auth_token_9876543210_test"

def charge_account(account_id, amount):  # VIOLATION: Missing type annotations & docstring
    # VIOLATION: Raw SQL string formatting vulnerable to SQL Injection
    sql = f"UPDATE accounts SET balance = balance - {amount} WHERE id = '{account_id}'"
    return sql
