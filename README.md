# shell-lib
## Outline
A command-line-interface of library genesis. Just like apt for e-books XD
## Install
```bash
pip install -r requirements.txt
```
## Usage
- Search for e-books
```bash
python3 main.py find <book-name>
```
- View downloaded books
```bash
python3 main.py cat
```
- Remove books
```bash
python3 main.py rm
```
- Change the source, which is https://libgen.is/ at default
```bash
python3 main.py chsrc <new-source>
```