# VAST

VAST - Visualise Abstract Syntax Trees for Python.

VAST generates ASTs for a given Python script and builds visualisations of them.

## How to use

From a python script:

```python
from vast import Vast

v = Vast("./helloworld.py")
# or
v = Vast()
ast = v.generateAST("./helloworld.py")
v.visualiseASTGraph(ast)
```

Or from the terminal:

```bash
$python vast.py ./helloworld.py
```
