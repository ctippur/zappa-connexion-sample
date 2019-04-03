# zappa-connexion-sample


# Create a virtual env
   * python3 -m venv --without-pip myvenv
   * source myvenv/bin/activate
   * curl https://bootstrap.pypa.io/get-pip.py | python
   * deactivate
   * source myvenv/bin/activate
   * pip install -r requirements.txt

# Test server locally
   * python -m swagger_server.app
   * curl -X GET "http://0.0.0.0:5000/" -H "accept: text/plain"

# Deploy to zappa
zappa deploy dev

# Test zappa
curl -X GET "https://um8wz2hhyh.execute-api.us-east-1.amazonaws.com/dev/" -H "accept: text/plain"
