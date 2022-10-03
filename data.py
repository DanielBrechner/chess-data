from secrets.py import api_key
import numpy as np
import matplotlib.pyplot as plt
import berserk
pip install berserk
session = berserk.TokenSession('api_key')
client = berserk.Client(session=session)
