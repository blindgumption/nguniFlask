# nguniFlask
experimenting with Nginx, Gunicorn, and Flask

##  Motivation 

I'm trying to understand WSGI and how gunicorn fits in the stack of a Python based web application.

## How It Works

I run this on Ubuntu 20.04 running under WSL2 on Windows 11.
I use Python 3.11 which you'll need to get from the deadsnakes apt repo (you can google for how to do that).
It probably works okay with Python 3.8 that comes with Ubuntu 20.04 though I have not tried that.

First, clone this repo.
I suggest creating and activating a virtual environment in the repo's directory.
Remember, if you have installed Python using apt on Ubuntu, you still need to install venv.  For example, 
``` bash
apt install python3.11-venv
```

With the venv activated, you can install all required modules with:
``` bash
pip install -r requirements.txt
```

Assuming everything installed okay, you can run gunicorn.
The config file has everything set for the dispatcher.py with all it's lovely hard-codings.  Run gunicorn simply as:
``` bash 
gunicorn
```

Now, you can hit http://ngunif.local:8000 from a curl command from another bash shell, or you can try your browser from Windows.

To use your windows browser, you'll first need to add ngunif.local to your windows hosts file (yeah, I didn't realize windows had a hosts file either).
I did this from powershell with admin using notepad.
The hosts file is in:
``` bash
C:\Windows\System32\drivers\etc
```
Add the line:
``` bash
127.0.0.1 ngunif.local 
```

Now you can open your favorite browser on windows and type:
``` bash
http://ngunif.local:8000
```
in the address bar and you should get a minimalst page from gunicorn.

Out of the box, dispatcher.py supports subdomains "home", "www", and "blog".
I have each of those in my hosts file as well though not sure they need to be there.

## 2023-07=07 Update

Oh boy did this get stale.
It's cleaned up some now though and working okay on Ubuntu 20.04 on WSL2 on Windows 11.
I'm no longer using Nginx and using this only to play around with gunicorn and flask. 

FYI: I wrote the how it works section along with this update, it should be acurate for a while :)
