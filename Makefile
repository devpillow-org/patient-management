create_local_environment:
	pip3 install virtualenv
	virtualenv -p python3 .venv

activate_local_environment:
	source .venv/bin/activate

run:
	fastapi dev code/main.py