import re
from urllib import request
import requests as req

url = "https://www.ceneo.pl/91714422"
response = req.get(url)
print(response.status_code)
