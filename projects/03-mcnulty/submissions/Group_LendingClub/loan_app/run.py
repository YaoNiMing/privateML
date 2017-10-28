#!/usr/bin/env python
from __future__ import absolute_import

import logging
from app import app as application

# logger = logging.getLogger("app")

def main(port=5000, debug=True):
    # logger.info("Staring App at Port: {} with Debug Option: {}".format(port, debug))
    application.run(port=port, debug=debug)


if __name__ == '__main__':
    main()
