.SILENT:
SHELL := /bin/bash
RUN_NEEDED_TARGETS := ${CEDAR_PATH} ${CEDAR_PATH}/venv ${CEDAR_PATH}/logs


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


build:

install:
	mkdir -p ${CEDAR_PATH}/logs

run_dev: ${RUN_NEEDED_TARGETS}
	cd ${CEDAR_PATH}; \
		source venv/bin/activate; \
		uvicorn app:app --app-dir ${CEDAR_PATH} --reload --log-config ./logging.ini

run:
