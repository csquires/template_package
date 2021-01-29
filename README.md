This repository is a template for the development of Python packages.

The best practices for package development include:
* **Documentation**: I prefer [numpy style](https://numpydoc.readthedocs.io/en/latest/format.html) docstrings, generated using [Sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html), and hosted on [ReadTheDocs](https://readthedocs.org/)
* **Testing**: I use the `unittests` package: https://docs.python.org/3/library/unittest.html.
* **Code coverage**: This shows how much of your code is actually run by your tests; I use https://about.codecov.io/

The below section shows what you'd actually put in the README.

# Main README

[![codecov](https://codecov.io/gh/uhlerlab/causaldag/branch/master/graph/badge.svg?token=RSM00FKU9A)](https://codecov.io/gh/uhlerlab/causaldag)

`template` is a Python package for ...

### Install
Install the latest version of `template`:
```
$ pip3 install template
```

### Documentation
Documentation is available at https://template.readthedocs.io/en/latest/


### Simple Example

```
>>> from template import mean
>>> import numpy as np
>>> x = np.array([1,2,3])
>>> mean(x)
2
```

### License

Released under the 3-Clause BSD license (see LICENSE.txt):
```
Copyright (C) 2021
[Author] <[email]>
```
