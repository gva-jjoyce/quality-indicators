#!/usr/bin/env python

import sys
import logging
from measures.maintainability import MaintainabilityTest
from measures.currency import CurrencyTest

logger = logging.getLogger("measures")
log_format = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
log_handler = logging.StreamHandler()
log_handler.setFormatter(log_format)
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)


results = []
results.append(MaintainabilityTest().test())
results.append(CurrencyTest().test())

if not all(results):
    logger.error('FAILURE')
    sys.exit(1)

logger.info('PASS')
