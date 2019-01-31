import json
import pymysql
from pymysql import OperationalError

class CredentialsNotFoundError(Exception):
	pass

def validate_db_credentials():
	with open("credentials.json") as file_obj:
		creds = json.loads(file_obj.read())
		for d in ["user", "password", "host", "db"]:
			if not creds.get(d):
				print("Please store database credentials in credentials.json file.")
				raise CredentialsNotFoundError

	try:
		connection = pymysql.connect(host=creds['host'], user=creds['user'], password=creds['password'],
			db=creds['db'], charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

		cursor = connection.cursor()
		cursor.execute("SELECT VERSION()")
		results = cursor.fetchone()
		# Check if anything at all is returned
		if results:
			globals()["connection"] = connection
		else:
			raise OperationalError
	except OperationalError as e:
		print("Cannot establish conncetion to database. Make sure the credentials are right.")
		raise OperationalError

if __name__ == "__main__":
	# validate credentials for database
	validate_db_credentials()
