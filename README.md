# PythonFlaskTest

1. python3 -m venv env
2. source env/bin/activate
3. pip install Flask
4. flask run

sample request for _**/api/v1/insert**_

```
curl --location --request POST 'http://127.0.0.1:5000/api/v1/insert' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data": 1
}'
```

sample request for _**/api/v1/get**_

```
curl --location --request GET 'http://127.0.0.1:5000/api/v1/get'
```

sample request for _**/api/v1/auto-insert**_
```
curl --location --request GET 'http://127.0.0.1:5000/api/v1/auto-insert'
```