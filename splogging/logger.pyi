"""Stub file for logger.py."""

import logging.handlers
from typing import Optional

def setup_logging(  # pylint: disable=too-many-arguments
    name: Optional[str] = ...,
    filename: str = ...,
    when: str = ...,
    backup_count: int = ...,
    file_level: Optional[str] = ...,
    file_format: Optional[str] = ...,
    file_log_datefmt: str = ...,
    console_level: Optional[str] = ...,
    console_format: Optional[str] = ...,
    console_log_datefmt: str = ...,
) -> logging.Logger: ...
