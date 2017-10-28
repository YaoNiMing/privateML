### mongoDB

If you already have Homebrew installed on your computer, do an update. Otherwise, you should get it first [here](http://brew.sh/).

```
brew update
```

```
brew install mongodb
```

Create a data directory, you may need to `sudo` it. Make sure the directory is read and write accessible for the current user with `chmod` if necessary.

```
mkdir -p /data/db
chmod -R 777 /data
```


If you want to have launchd start mongodb now and restart at login:
```
brew services start mongodb
```  

if you don't need a background service, just run

```
mongod
```
You can kill it with Ctrl+C later.

Start a new terrminal window. Connect to the mongoDB server with `mongo`.

```
help
show dbs
use new_cool_db
show dbs
```


So what’s happening when you run `mongod`?
- You run a service (background process) that *is* the database.  
- It sits and waits for a connection from clients that want to use the database (on a certain port, just like Flask uses 5000).
- It will stop running as soon as you close your terminal window or do Ctrl+C.

So what’s happening when you run `brew services start mongodb`?
- The same service runs as with `mongod`.
- *EXCEPT*: This runs completely in the background.  If you close your terminal, it keeps running.  This is what you want for a real database, which would be available for queries at all times.

So what’s happening when you run `mongo`?
- You create a *Mongo DB shell client* to make a connection to the server (`mongod`) and query it.
- This is just one type of client that you can use to query a MongoDB database.  Likely, you’ll also use a Python client like `pymongo`.


