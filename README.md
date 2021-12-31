# VAST

VAST - Visualise Abstract Syntax Trees for Python.

VAST generates ASTs for a given Python script and builds visualisations of them.

## How to use

From a python script:

```python
from vast.vast import Vast

v = Vast("./helloworld.py")
# or
v = Vast()
ast = v.generateAST("./helloworld.py")
v.visualiseASTGraph(ast)
```

Or (if installed from source, rather than pip) from the terminal:

```bash
$python vast.py ./helloworld.py
```

## Like what you see?  Buy me a snack

If you want to see more of what I do, you can visit [my blog](https://jamesphillipsuk.com "Go there now").

If you want to donate to my development work by buying me a snack, I use [PayPal.Me](https://paypal.me/JamesPhillipsUK "My PayPal.Me").
