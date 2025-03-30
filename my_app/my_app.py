#!/usr/bin/env python3.11

import logging
from logging import NullHandler
from domain import ModelError, User

logging.getLogger(__name__).addHandler(NullHandler())
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

if __name__ == '__main__':
    try:
        user = User(id=1, name="Alice")
        logging.info(f"User created: {user}")
    except ModelError as e:
        logging.warning(f"Model error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
