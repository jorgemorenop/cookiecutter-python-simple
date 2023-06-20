# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Quickstart

This is a project generated with [cookiecutter](https://github.com/cookiecutter/cookiecutter). 
Here is a quick explanation of the things you will find in this repository. 


### Python code

This simple repository includes the resources to build a single python package for a library or application. You could
easily add more packages once created (just create the folders and add the references in pyproject), but if you need
more complex needs (different dependencies per package, etc.), you'll have to tweak the structure a bit (for instance,
having pyproject.toml per package).


### Setup development environment
To start working in the project and installing the dependencies, it's **highly recommended** that you create
a Python virtual environment:

```bash
python -m venv venv/
source venv/bin/activate
```
 (you can choose other tools for this if you are already familiar with them).

Once you are in your newly created environment, you can install the package (in editable mode) and its dev dependencies
by running:

```bash
python -m pip install -e '.[dev]'
```

### Running tests

You can create new unit tests in the `tests/` folder.

After setting up your dev environment, you will be able to use `pytest` to run your tests with:

```bash
python -m pytest tests/
```

### Static analysis and formatting
We have setup some tools that perform static analysis in our code to ensure that we always follow the best practices:

- mypy: A typing static analysis tool. Although typing is optional in Python, this tool makes it mandatory (kind of like going from Javascript to Typescript). It ensures that the types of the variables and functions' parameters and responses are always coherent. Run with `mypy {{cookiecutter.package_name}}/`.
- ruff: A linting tool, similar to flake8, but faster. It can warn you about different kind of errors, depending on the configuration (bad practices, wrong import errors, memory leaks, unused variables, ...). Run with `ruff .`.
- black: A very opinionated code formatting tool. Run with `black .`
