# World-Stats-Scrapper

Scrape world stats info from https://www.internetworldstats.com/list2.htm

### Prerequisites

- Python2 (haven't tested on Python3)
- MySql
- Follow the steps from here to create a new mysql user and databse. Grant the user (select, delete, update, insert, create) privileges - [Create MySql db and user](https://www.lanexa.net/2011/08/create-a-mysql-database-username-password-and-permissions-from-the-command-line/)

### How to run

- Clone the repo on your system (directly or through virtualenv)
```bash
git clone https://github.com/Zlash65/World-Stats-Scrapper.git
cd World-Stats-Scrapper/
```
- Install the requirements
```bash
pip install -r requirements.txt
```
- Open the credentials.json file and add the mysql credentials that you created in Prerequisites step.
```bash
# Something like this

{
	"user": "db_user",
	"password": "db_password",
	"db": "test_db",
	"host": "localhost"
}
```
- Now, simply execute the generator file
```bash
python generator.py

# if matplotlib throws an error saying python not installed as framework or so
# follow the following commands
cd ~/.matplotlib
vim matplotlibrc

# in vim shell, write the following instruction
backend: TkAgg

# save and exit vim shell and run the generator file once again
python generator.py
```
- The generated output should automatically open in a browser tab. Incase it does not open on its own, look for the index.html file in html folder and open it in browser.
