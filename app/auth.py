import urllib2  # VIOLATION: Deprecated package

# VIOLATION: Hardcoded plaintext secret
API_SECRET_KEY = "ghp_1234567890abcdef1234567890abcdef"

# VIOLATION: Missing type hints and docstring
def find_user(username):
    # VIOLATION: Raw f-string SQL query (SQL injection vulnerability)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query
