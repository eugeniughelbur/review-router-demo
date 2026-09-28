"""Checks run on user input before it reaches the filesystem."""

import os


def safe_path(root: str, name: str) -> str:
    """Resolve a user-supplied file name inside root."""
    return os.path.normpath(os.path.join(root, name))
