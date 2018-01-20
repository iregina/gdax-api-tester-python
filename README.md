# The GDAX API Tester - Python
Quick and easy program to test GDAX API endpoints in Python

## Getting Started
For those who are totally brand new to Python (like me). 

##### 1. In terminal, download Python
```$ sudo easy_install pip```

##### 2. Requires python-requests. Install with pip:
```$ pip install requests``` or ```$ easy_install requests```

##### 3. Fork this repository by clicking "fork" in the top-right corner of the page.

##### 4. Set up Git and make sure you have set up authentication to Github.

##### 5. Navigate to your fork of this repository and under the repository name, click Clone or Download.

##### 6. In either the clone with HTTP or SSH section, click the copy icon to copy the clone URL for the repository. 

##### 7. In terminal, type git clone, and then paste the URL you copied in Step 2. It will look like this, with your GitHub username instead of YOUR-USERNAME:
```$ git clone https://github.com/YOUR-USERNAME/gdax-api-tester-python```

##### 8. Open up the repository in terminal and create a config.py file:
```$ touch config.py```

##### 9. Go to https://www.gdax.com/settings/api, select all the necessary permissions, and create an API Key.

##### 10. Open the config.py in your text editor, and include your API Key, API Secret, and Passphase like this:
```api_key = "[your key here]"
api_secret = "[your secret here]"
passphrase = "[your passphrase here]"
```

## Running your app
Now let's get started. 

#### 1. In terminal, go to your gdax-api-tester-python repository and run:
```python gdax-test.py```

#### 2.  You will see the following question: 
``` Hello. Welcome to GDAX API Tester in Python!

These are the following options:
1) balance -> see your gdax wallet balances
2) id -> see your wallet account ids
3) order -> place an order
```


Enter ```balance``` in the terminal to see all of your GDAX wallet balances

Enter ```id``` to see the wallet account ids of all your GDAX wallets

Enter ```order``` to place a GDAX order






