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
* GET /ticket/types
* GET /ticket/priorities

* GET /ticket/all
* GET /ticket/backlog
* GET /ticket/<id>
* POST /ticket
* DELETE /ticket/<id>
* PATCH /ticket/<id>


* GET /ticket/{id}/comment/all
* POST /ticket/{id}/comment/all
* GET /ticket/{id}/comment/{comment_id}
* DELETE /ticket/{id}/comment/{comment_id}
* PATCH /ticket/{id}/comment/{comment_id}
  

* GET /board/all
* GET /board/{id}
* POST /board
* PATCH /board/{id}
* DELETE /board/{id}
  
* GET /user/all
* GET /user/{email}
* DELETE /user/{email}

* POST /register
* POST /login
* POST /role

