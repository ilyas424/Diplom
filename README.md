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

![image](https://github.com/ilyas424/Diplom/assets/107006539/39109e8e-fd50-4011-9b64-12808b06b20e)
  
![image](https://github.com/ilyas424/Diplom/assets/107006539/a1175172-6426-48b3-be37-55a205d7a3b0)
![image](https://github.com/ilyas424/Diplom/assets/107006539/ca96ed34-530f-46dd-89f1-110181eee8ba)
![image](https://github.com/ilyas424/Diplom/assets/107006539/32fb1199-04d2-463f-a7fe-17bd5ca6f989)

  
![image](https://github.com/ilyas424/Diplom/assets/107006539/b1d104d5-c30c-4cb7-b084-82c7b4599553)
  
![image](https://github.com/ilyas424/Diplom/assets/107006539/8cba5f3d-2c7f-4c49-895e-7fcf97f43c4e)
  
![image](https://github.com/ilyas424/Diplom/assets/107006539/c44fa6a3-2932-4c80-a3b5-0b599d2693fa)

![image](https://github.com/ilyas424/Diplom/assets/107006539/01fd1fca-bfe1-47af-9be9-2c3701263001)

![image](https://github.com/ilyas424/Diplom/assets/107006539/e449fb21-db58-4f4d-b7b6-aaef1df56080)

![image](https://github.com/ilyas424/Diplom/assets/107006539/0b20b9b7-5517-4108-be9f-6a5596bed346)

![image](https://github.com/ilyas424/Diplom/assets/107006539/d00955c3-4591-4c16-b964-e4ff39f6afe8)

![image](https://github.com/ilyas424/Diplom/assets/107006539/252236e4-65ee-4e5f-bfe0-f04c2364a2b9)

![image](https://github.com/ilyas424/Diplom/assets/107006539/f2b7f0b2-404a-4b71-aa35-de6fca108c17)

  


  

