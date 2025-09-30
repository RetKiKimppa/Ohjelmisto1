from enum import Enum
import mysql.connector
import os
import math
from dataclasses import dataclass
from geopy.distance import geodesic

conn = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='bosstest',
         user='kim',
         password='1111',
         autocommit=True
         )



