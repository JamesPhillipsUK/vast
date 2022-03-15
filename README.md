# VisAST

VisAST - Visualise Abstract Syntax Trees for Python.

VisAST generates ASTs for a given Python script and builds visualisations of them.

## Install

Install from PyPI [Here!](https://pypi.org/project/VisAST/)

## How to use

From a python script:

```python
from visast import generate, visualise

ast = generate.fromPath("./helloworld.py")
visualise.graph(ast)
# or
pyString = "print(\"Hello, World!\")"
ast = generate.fromromString(pyString)
visualise.graph(ast)
# or
pyURL = "https://example.com/helloworld.py"
ast = generate.fromURL(pyURL)
visualise.graph(ast)

```

## Like what you see?  Buy me a snack

If you want to see more of what I do, you can visit [my blog](https://jamesphillipsuk.com "Go there now").

If you want to donate to my development work by buying me a snack, I use [PayPal.Me](https://paypal.me/JamesPhillipsUK "My PayPal.Me").
