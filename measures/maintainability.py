"""
Maintainability Index Tester

Uses radon to calculate Maintainability Index
(see: https://radon.readthedocs.io/en/latest/intro.html)


Files in /tests/ folder are excluded, as well as as there being an option to
add a flag to the file to exclude specific files.

Radon itself will A grade for maintainability for scores 100 to 20, this
script sets the bar at 50.
"""
import radon.metrics
import logging
import glob
import sys

logger = logging.getLogger("measures")

EXCLUSIONS = ['./tests/']
LIMIT = 50

class MaintainabilityTest():

    def __init__(self):
        pass

    def test(self):

        file_list = glob.iglob('./**/*.py', recursive=True)
        results = []

        for item in file_list:
            if any([True for exclusion in EXCLUSIONS if item.startswith(exclusion)]):
                continue

            with open(item, 'r', encoding='UTF8') as code_file:
                code = code_file.read()

            maintainability_index = radon.metrics.mi_visit(code, True)

            if code.startswith('#no-maintain-checks'):
                logger.info(F"{item:20} {maintainability_index:.2f} - skipped")
                results.append('SKIPPED')
                continue

            if maintainability_index <= LIMIT:
                results.append('FAILED')
                logger.error(F"{item:20} {maintainability_index:.2f} - below {LIMIT}")
            else:
                results.append('PASSED')

        logger.info(F"MAINTAINABILITY INDEX: {results.count('PASSED')} passed, {results.count('FAILED')} failed, {results.count('SKIPPED')} skipped")

        return results.count('FAILED') == 0
