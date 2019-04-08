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

# Swagger link
   You can also check the swagger link here.
   * http://0.0.0.0:5000/ui/

# Deploy to zappa
zappa deploy dev

# Test zappa
curl -X GET ```http://<endpoint>/dev/``` -H "accept: text/plain"
