**quality-indicators** are a set of tests which should be run against most Python repositories.

## maintainability

Calculates a [Maintainability Index](https://radon.readthedocs.io/en/latest/intro.html) score for each Python module found outside the `tests` folder - it will report a failure if any module scores lower than 65.

## currency

This is a simple composition analysis scanner for Python; it uses the manifest of currently installed packages as the composition, then looks up components on PyPI to determine the latest version and a list of vulnerable components maintained by pyup to determine if any have security weaknesses. It will report failure if more than 20% of packages are stale. 
