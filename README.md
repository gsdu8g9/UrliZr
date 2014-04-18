[![Build Status](http://drone.luxiferapp.com/github.com/luxifer/UrliZr/status.svg?branch=master)](http://drone.luxiferapp.com/github.com/luxifer/UrliZr)

Installation
============

Settings.py
-----------

The you can start the dev server by launching:

```bash
pip install -r requirements.txt
export DATABASE_URL="mysql://user:pass@host/db"
python manage.py syncdb
foreman start
```

API (WIP)
---------

This URL shortener also provide a useful API to integrate in your website
You can retrieve shortened URL in raw, json or xml format just via this url:

`http://<your host>/api/translate/<method>`

You just have to pass POST parameters with url containing the url you want to shortened
