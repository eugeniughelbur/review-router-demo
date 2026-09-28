"""Checks run on user input before it reaches the filesystem."""

import os


def safe_path(root: str, name: str) -> str:
    """Resolve a user-supplied file name inside root, or refuse."""
    if ".." in name or name.startswith("/"):
        raise ValueError("path escapes the upload folder")
    path = os.path.normpath(os.path.join(root, name))
    if not path.startswith(os.path.normpath(root) + os.sep):
        raise ValueError("path escapes the upload folder")
    return path
