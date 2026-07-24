from client import RuntimeAiAuthorizationGuardClient

def main():
    client = RuntimeAiAuthorizationGuardClient()
    res = client.authorize("python -m unittest test_api.py", "./tests")
    print(f"Authorized: {res['is_authorized']}")
    print(f"Decision: {res['security_decision']}")

if __name__ == "__main__":
    main()
