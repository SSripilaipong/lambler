pull-data-start:
	pytest -m start_pull_data

pull-data:
	pytest -m pull_data

pull-data-stop:
	pytest -m stop_pull_data

release:
	rm -rf ./dist || exit 0
	python setup.py sdist
	twine upload dist/*
