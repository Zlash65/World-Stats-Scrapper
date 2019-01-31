from bs4 import BeautifulSoup
import requests, json
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

def scrape_and_retrieve_data():
	# url that we are targetting for this specific scraping
	url_to_scrape = "https://www.internetworldstats.com/list2.htm"

	# use beautifulsoup to get the html content of the site
	page_response = requests.get(url_to_scrape, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")

	# data that we want to retrieve is stored in table with attribute summary=data2
	data_table = [d for d in page_content.find_all('table') if d.get("summary") == "data2"]

	# retrieve headers from the first row element
	headers = [k.text for k in data_table[0].find_all('tr')[0].find_all('b')]
	headers = [k.replace('\r\n', ' ') if '-' not in k else k.replace('\r\n-', '') for k in headers]

	# retrieve data that falls under the required headers
	data = []
	for i in data_table:
		for j, k in enumerate(i.find_all('tr')):
			if j == 0: continue # ignore headers row
			temp = list(filter(None, k.text.replace('\r\n%', ' %').replace('\r\n', '').split('\n')))
			if temp[1]=="--": temp[1] = temp[0]
			data.append(temp)

	globals()["headers"] = headers
	return headers, data

if __name__ == "__main__":
	# validate credentials for database
	validate_db_credentials()
