"""File hashing helpers used for data manifests."""

import hashlib
import os

CHUNK_SIZE = 1024 * 1024  # bytes read per iteration (1 MiB)


def sha256_file(path: str | os.PathLike[str]) -> str:
    """Return the lowercase hex SHA-256 of the file at ``path``, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()
