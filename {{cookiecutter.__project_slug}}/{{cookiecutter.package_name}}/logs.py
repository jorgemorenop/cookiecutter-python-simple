import logging
import os
import sys
{% if cookiecutter.__min_python_subversion|int < 10 %}from typing import Optional
{% endif %}
{% if cookiecutter.__min_python_subversion|int < 10 %}
def setup_logging(name: Optional[str] = None) -> logging.Logger:{% else %}
def setup_logging(name: str | None = None) -> logging.Logger:{% endif %}
    """Set up logging for the application."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    )
    logger.setLevel(os.getenv("log_level", "INFO"))
    logger.addHandler(handler)
    logger.propagate = False
    return logger
