[[elements]]
author = "u/HiT3Kvoyivoda"
tags = "scraping"
body = """
Mine is a web scraper. It's only like 50 lines of code.

It takes in a link, pulls all the hyperlinks and then does some basic regex to pull out the info I want. Then it spits out a file with all the links.

Took me like 20 minutes to code, but I feel like I use it every other week to pull a bunch of links for files I might want to download quickly or to pull data from sites to model.
"""

[[elements]]
author = "u/lagerbaer"
tags = "picture"
body = """
It's really basic but my mom has a digital picture frame that you can email pictures to. Once a week I grab pics I want to send to her frame from Google Photos (not automatically because the Google Photo API sucks ass) and download them. Then I use the script to email them to the frame; the only "business logic" there is that I need to split it up into chunks of 25 MB each.
"""

[[elements]]
author = "u/IndianaJoenz"
tags = "app"
body = """
https://github.com/cmang/durdraw is an ascii art editor I made that started out in 2009 as a 193-line Python 2 script. It could do some very primitive editing and saving, nothing else. Not even load. I was very much a "play with curses, learning python" project.

I soon added animation, because the other editors I was using did not have that feature, and color. Eventually ported it to Python 3, added more features, more colors, got other people using and contributing to it.

15 years and many incremental changes later, it's doing pretty good now, for its niche (ANSI art editors). I still use it daily.
"""

[[elements]]
author = "u/voxcon"
body = """
My mom had a difficult time remembering when she opened certain things in the fride. I suggested, she should use a pen and write the date down. She somehow didn't like that idea.

Since she didn't like that idea i frankensteined together a raspberry pi, a label printer, a few physical push buttons and some leds. Now she can simply press a button to print a perfectly sized sticky label with the current date and time on it. Somehow she likes this solution and uses it daily.

In the background there runs a python script waiting for inputs. Once it detects that the print button is pressed it fetches the local date and time from a list of ntp servers, converts it info a printable pdf displaying the data and sends the print command over to the label printer. The printer then prints and cuts the label to size and you can stick it wherever you want.

Been in daily use for about 5 to six years. Still going strong.
"""

[[elements]]
author = "u/Wallstreetbettss"
body = """
I have one that it took me 5-10 mins to build and I have it running 24/7 on task scheduler since early 2022. It's a laptop mouse shaker, it slightly moves every 10 mins.I work for a finance company that's is a big brother.

Our internal system flags gets flagged every 15 mins that there's no interaction with the pc while you are logged in. And when that happens, managers get an automated email to check in with that person since we're wfh.
"""