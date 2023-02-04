Запуск приложения:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r ./requirements.txt
# развернуть бд и накатить миграции
uvicorn app:app --reload
python3 ./initial_db_data.py
```

Миграции:

```bash
alembic revision --autogenerate -m <text>
alembic upgrade head
```

API:
* GET /ticket/type/all
* GET /ticket/priority/all
* GET /ticket/status/all
* GET /employee/all
* GET /employee/<id>
* POST /comment <- id
* GET /comment/<id>
* DELETE /comment/<id>
* PATCH /comment/<id> # only for TEXT
* GET /ticket/<id>
* GET /ticket/all
* DELETE /ticket/<id>
* PATCH /ticket/<id>
