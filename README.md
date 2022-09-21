
# Domino

### Before use (for test purposes):
```
pip install -r requirements.txt
```

### Launch tests (in repository root):
```
pytest
```

### Usage:
```
domino.py [-h] [-v] --row ROW [--moves MOVES]

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --row ROW, -r ROW     Set the playing board. Please remember, that allowed characters are: \, /, |
  --moves MOVES, -m MOVES
                        Set the number of moves. The type must be positive integer or 0
```

### Example (in repository root):

```
python domino/domino.py --row '|/||||\\|/|' --moves 2 
```
