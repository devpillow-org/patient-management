install:
	pip3 install -r requirements.txt
serve:
	mkdocs serve

deploy:
	mkdocs gh-deploy