import os

from deta import Deta
from dotenv import load_dotenv


load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

#DETA_KEY = "c05dxhya_NtnzLiZoJDZrAgZ7mqmvGRzVornhzVBt"

# Initial with a ptoject key
deta = Deta(DETA_KEY)

#this is how to create/connect a database
db = deta.Base("users_db")

def insert_user(username, name, password):
	"""returns the user on a successful user creation, otherwise raises and error"""

	return db.put({"key":username,"name":name,"password":password})


def fetch_all_users():
	"""returns a dict of all users"""
	res = db.fetch()
	return res.items

def get_user(username):
	"""if not found, the will return none"""
	return db.get(username)

def update_user(username, updates):
	return db.update(updates, username)

def delete_user(username):
	return db.delete(username)
