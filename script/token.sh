curl -i \
  -H "Content-Type: application/json" \
  -d '
{ "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "default" },
          "password": "ADMIN_PASS"
        }
      }
    }
  }
}' \
  "http://localhost:5000/v3/auth/tokens" ; echo
