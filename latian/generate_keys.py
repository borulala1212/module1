import pickle 
from pathlib import Path

import streamlit_authenticator as stauth

## usernames:
#    jsmith:
#      email: lala@gmail.com
#      name: lala la
#      password: 123 # To be replaced with hashed password
#    rbriggs:
#      email: nana@gmail.com
#      name: nana na
#      password: 456 # To be replaced with hashed password
#cookie:
#  expiry_days: 30
#  key: some_signature_key
#  name: some_cookie_name
#preauthorized:
#  emails:
#  - melsby@gmail.com


names = ["Peter Parker","Hermeoni"]
usernames = ["PP","HM"]
password = ["XXX","XXX"]

hashed_passwords = stauth.Hasher(['123','456']).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
	pickle.dump(hashed_passwords, file)
