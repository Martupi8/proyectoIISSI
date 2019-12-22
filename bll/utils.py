# This file is part of the Silence framework.
# Silence was developed by the IISSI1-TI team
# (Agustín Borrego, Daniel Ayala, Carlos Ortiz, Inma Hernández & David Ruiz)
# and it is distributed as open source software under the GNU-GPL 3.0 License.

from bll.BLLException import BLLException

def check_not_null(value, msg):
    if value is None or (isinstance(value, str) and value.strip() == ""):
        raise BLLException(msg)
