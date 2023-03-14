.SILENT:
SHELL := /bin/bash
RUN_DEV_NEEDED_TARGETS := ${CEDAR_PATH} ${CEDAR_PATH}/venv ${CEDAR_PATH}/logs


test_env:
	echo CEDAR_PATH=${CEDAR_PATH}
	echo CEDAR_DB_HOST=${CEDAR_DB_HOST}
	echo CEDAR_DB_NAME=${CEDAR_DB_NAME}
	echo CEDAR_DB_USER_NAME=${CEDAR_DB_USER_NAME}
	echo CEDAR_DB_USER_PASSWORD=${CEDAR_DB_USER_PASSWORD}

install_venv: ${CEDAR_PATH}
	cd ${CEDAR_PATH}; \
		virtualenv -p python3 venv; \
		source venv/bin/activate; \
		pip3 install --no-cache -r requirements.txt

install_postgresql:
	sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'; 
	wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -; 
	sudo apt-get update; 
	sudo apt-get -y install postgresql; 


build_postgresql:
	build_postgresql:
	sudo -i -u postgres createuser -s ${CEDAR_DB_USER_NAME};\
	sudo -u  postgres psql -c 'CREATE DATABASE "${CEDAR_DB_NAME}" OWNER ${CEDAR_DB_USER_NAME}'; \
	sudo -u  postgres psql -c "ALTER ROLE ${CEDAR_DB_USER_NAME} WITH PASSWORD '${CEDAR_DB_USER_PASSWORD}' "; 

build:

install:

run:


build_dev:

install_dev:
	mkdir -p ${CEDAR_PATH}/logs

run_dev: ${RUN_DEV_NEEDED_TARGETS}
	cd ${CEDAR_PATH}; \
		source venv/bin/activate; \
		uvicorn app:app --app-dir ${CEDAR_PATH} --reload --log-config ./logging.ini
