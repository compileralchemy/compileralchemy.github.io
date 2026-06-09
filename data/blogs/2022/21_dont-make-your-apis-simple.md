title: Don't make your APIs simple
---
Hussein Nasser says: \"Don't make your APIs simple\". Meaning, prefer default configs over abstractions as, when things break, developers get to some options to fix around.

"They are back to the same sinking ship, except at least this sinking ship has a lifeboat attached to it that a developer may cling to. They look at the default values and understand what went wrong and override them if necessary."

I did not take it in that sense when i implemented the idea in meteomoris. For me, it was a conscious choice to let developers have added power.

```python
from meteomoris import Meteo
from meteomoris import get_main_message

Meteo.CHECK_INTERNET = True # Will check if there is internet
Meteo.EXIT_ON_NO_INTERNET = True # Will exit if no internet
Meteo.ALREADY_CHECKED_INTERNET = False
Meteo.DEBUG = False # used during development
Meteo.CACHE_PERMS = True # used internally, modify to refelct if cache file can be created
Meteo.CACHE_PATH = "." # If cache path can be customized, default to  site-packages

Meteo.today = "2023-11-10" # If you want to override cache data
Meteo.headers = {
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',
         'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
         'Accept-Language' : 'en-US,en;q=0.5', 
         'Accept-Encoding' : 'gzip', 
         'DNT' : '1', # Do Not Track Request Header 
         'Connection' : 'close',
         'Sec-GPC': '1',
         'Sec-Fetch-Site': 'none',
         'Sec-Fetch-Mode': 'navigate',
         'Sec-Fetch-User': '?1',
         'Connection': 'keep-alive',
         'Upgrade-Insecure-Requests': '1'
     } # Redefine default headers here
print(get_main_message())
```

Article: 
https://lnkd.in/esA8aVnK

Metemoris package: 
https://lnkd.in/gJkTuCis
