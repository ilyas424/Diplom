Запуск приложения:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r ./requirements.txt
# развернуть бд и накатить миграции
uvicorn app:app --reload
python3 ./initial_db_data.py
cd frontend
npm run serve
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
  
EDR - диаграмма 

![image](https://github.com/ilyas424/Diplom/assets/107006539/6d1a53aa-9a7e-43a3-ad6d-2b2f42871917)
  
![image](https://github.com/ilyas424/Diplom/assets/107006539/e2462c75-0cdb-4258-b43c-70d83d5610b4)
![image](https://github.com/ilyas424/Diplom/assets/107006539/f91ed026-b63a-4b0b-b847-b2802d458f73)
![image](https://github.com/ilyas424/Diplom/assets/107006539/6a5f5c29-518e-4702-82cf-1b9164a3201b)
  
![image](https://github.com/ilyas424/Diplom/assets/107006539/e59b7c03-3bd6-45e9-bc56-6bb00e30696b)

  
![image](https://github.com/ilyas424/Diplom/assets/107006539/7723e468-ba79-40c1-aa3d-be0f66136f59)

![image](https://github.com/ilyas424/Diplom/assets/107006539/74730e3c-a3c7-41d3-a43b-672576b41ffe)

![image](https://github.com/ilyas424/Diplom/assets/107006539/f9fe6f66-cf14-4769-8e11-abe50ce091f4)

![image](https://github.com/ilyas424/Diplom/assets/107006539/91afb66d-46b4-4625-813a-51dfbc513243)

![image](https://github.com/ilyas424/Diplom/assets/107006539/3bce4dc7-654f-4c2a-b2bb-650d173af375)

![image](https://github.com/ilyas424/Diplom/assets/107006539/91106cb9-8302-40c5-b6e9-a22b01fab1bc)

![image](https://github.com/ilyas424/Diplom/assets/107006539/79ba368d-e11a-407b-9490-2af0054f64d5)

![image](https://github.com/ilyas424/Diplom/assets/107006539/f4b7aed7-6059-43ad-88f5-6fe7240052d9)

  

