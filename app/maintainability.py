"""
Maintainability Index Tester

Uses radon to calculate Maintainability Index
(see: https://radon.readthedocs.io/en/latest/intro.html)

Tools & Tests are excluded, as well as as there being an option to add a flag
to the file to exclude spefific files.

Radon itself will A grade for maintainability for scores 100 to 20, this
script sets the bar at 65.
"""
import radon.metrics
import logging
import glob
import sys

EXCLUSIONS = ['/tests/']
LIMIT = 65

class MaintainabilityTest():

    def __init__(self):
        pass

    def test(self):

        file_list = glob.iglob('./**/*.py', recursive=True)
        failed_tests = 0
        results = []

        for item in file_list:
            if any([True for exclusion in EXCLUSIONS if item.startswith(exclusion)]):
                continue

            with open(item, 'r', encoding='UTF8') as code_file:
                code = code_file.read()

            maintainability_index = radon.metrics.mi_visit(code, True)

            if code.startswith('#no-maintain-checks'):
                logging.info(F"{item:20} {maintainability_index:.2f} - skipped")
                results.append('SKIPPED')
                continue

            if maintainability_index <= LIMIT:
                all_okay = False
                results.append('FAILED')
                logging.error(F"{item:20} {maintainability_index:.2f} - below {LIMIT}")
            else:
                results.append('PASSED')

        logging.error(F"MAINTAINABILITY INDEX: {results.count('PASSED')} passed, {results.count('FAILED')} failed, {results.count('SKIPPED')} skipped")

        return results.count('FAILED') > 0