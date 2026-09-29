# Flask and MongoDB

DevOps assignment – Flask JSON API + form that saves to MongoDB Atlas.

Student: Shankar Anand

GitHub: https://github.com/shankar-anand1/Flask_and_MongoDB_ShankarAnand

## Run

```
pip install -r requirements.txt
python3 app.py
```

Open http://127.0.0.1:5000

JSON API: http://127.0.0.1:5000/api

## MongoDB Atlas

In `app.py` replace USERNAME, PASSWORD and the cluster host in MONGO_URI.
Or set environment variable:

```
export MONGO_URI="mongodb+srv://user:pass@cluster0.xxxxx.mongodb.net/"
```

Also allow your IP in Atlas Network Access.
