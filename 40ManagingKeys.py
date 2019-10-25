# .env file
DATABASE = Sample_Connection_String

# app.py
from dotenv import load_dotenv
import os
load_dotenv()
database = os.getenv('DATABASE')
print(database)