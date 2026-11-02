# Piano: lab/hashing.py — sha256_file

## Obiettivo
Aggiungere `sha256_file(path)` in `lab/hashing.py`: restituisce lo SHA-256 esadecimale (minuscolo, 64 caratteri) di un file letto a blocchi. Serve ai manifest dei dati (AGENTS.md: ogni file scaricato ha SHA-256).

## Criteri di accettazione
- `sha256_file` accetta `str` o `os.PathLike`, apre il file in modalità binaria, lo legge a blocchi di costante `CHUNK_SIZE = 1 MiB` (1024*1024) e aggiorna un `hashlib.sha256`.
- Contenuto "abc" -> `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`.
- File vuoto -> `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- File più grande di un blocco (letterale indipendente `2 * 1024 * 1024 + 123` byte, contenuto `bytes((i * 31 + i // 251) % 256 for i in range(n))`, che non si ripete ai confini di 1 MiB) -> uguale a `hashlib.sha256(contenuto).hexdigest()`. Un test separato asserisce `CHUNK_SIZE == 1024 * 1024`.
- File inesistente: l'eccezione `FileNotFoundError` si propaga (nessun try/except).

## Approccio
- `lab/hashing.py`: docstring e commenti in inglese, nessuna dipendenza oltre la stdlib (`hashlib`, `os`/`pathlib`).
- `tests/test_hashing.py`: tre test richiesti con `tmp_path`; il test multi-blocco usa il letterale indipendente (non la costante del modulo). Più un test su `CHUNK_SIZE` e uno per `FileNotFoundError`.
- Non-obiettivi: nessuna API per manifest, nessun altro algoritmo, nessuna modifica a `docs/DECISIONS.md`.

## Assunzioni
- Python 3.12 / uv già configurati (`pyproject.toml`); nessuna nuova dipendenza.
- La funzione non produce numeri di backtest; i valori attesi sono vettori noti SHA-256 standard.

## Verifica
- `uv run pytest` -> tutti i test passano (smoke + 5 nuovi).
- Branch di lavoro: `feat/hashing` (già attivo). Commit solo a test verdi; nessuna PR, nessun push.
