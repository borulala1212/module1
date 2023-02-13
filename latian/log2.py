import streamlit_authenticator as stauth 

import database as db

usernames = ["mm","vv"]
names = ["mama","vava"]
passwords = ["123","abc"]
hashed_pasword = stauth.Hasher(passwords).generate()

for (username, name, hash_password) in zip(usernames, names, hashed_pasword):
	db.insert_user(username, name, hash_password)