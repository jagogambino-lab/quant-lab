import hashlib

import pytest

from lab.hashing import CHUNK_SIZE, sha256_file


def test_chunk_size_is_one_mib():
    assert CHUNK_SIZE == 1024 * 1024


def test_abc(tmp_path):
    p = tmp_path / "abc.txt"
    p.write_bytes(b"abc")
    assert (
        sha256_file(p)
        == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    )


def test_empty_file(tmp_path):
    p = tmp_path / "empty.bin"
    p.write_bytes(b"")
    assert (
        sha256_file(p)
        == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )


def test_multi_chunk_file_matches_hashlib(tmp_path):
    n = 2 * 1024 * 1024 + 123  # independent of CHUNK_SIZE on purpose
    content = bytes((i * 31 + i // 251) % 256 for i in range(n))
    p = tmp_path / "big.bin"
    p.write_bytes(content)
    assert sha256_file(str(p)) == hashlib.sha256(content).hexdigest()


def test_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        sha256_file(tmp_path / "nope.bin")
