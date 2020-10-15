lint:
	python3 -m isort --gitignore .
	python3 -m black .
	python3 -m pylint splogging
	python3 -m flake8 --extend-exclude venv,build
	python3 -m mypy splogging
	python3 -m pydocstyle splogging

test:
	python3 -m pytest
	tox

build:
	python3 setup.py sdist bdist_wheel
	twine check dist/*

upload:
	twine upload dist/*

.PHONY: build
