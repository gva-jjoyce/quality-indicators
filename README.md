**quality-indicators** are a set of simple quality measures for Python libraries.

## Maintainability

Calculates a [Maintainability Index](https://radon.readthedocs.io/en/latest/intro.html) score for each Python module found outside the `tests` folder.

**Quality Bar**: All modules exceed 50

## Currency

This is a simple composition analysis scanner for Python; it uses the manifest of currently installed packages as the composition, then looks up components on PyPI to determine the latest version and a list of vulnerable components maintained by pyup to determine if any have security weaknesses. 

**Quality Bar**: Less than 20% of components STALE  
**Quality Bar**: 0 components with known weaknesses


# Example Workflow
~~~yaml
name: integration_tests
on: [push, pull_request]
jobs:
  quality_measures:
    runs-on: ubuntu-latest
    steps:
      - name: check out
        uses: actions/checkout@v2
  
      - name: set up
        uses: actions/setup-python@v2
        with:
          python-version: '3.8' 

      - name: install component base requirements
        run:  pip install -r $GITHUB_WORKSPACE/requirements.txt

      - name: execute_action
        uses: gva-jjoyce/quality-indicators@main
~~~