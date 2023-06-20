
install:
	pip install -e '.[dev]'
test:
	pytest tests/unit/
analyze:
	black . --check
	ruff .
	mypy {{cookiecutter.package_name}}/
