import pyodbc
from sqlalchemy import create_engine
from urllib import parse

connection_str="Driver={ODBC Driver 18 for SQL Server};Server=tcp:gnvadev.database.windows.net,1433;Database=mid_sandbox;Uid={Siddharth.Mandal@shell.com};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;Authentication=ActiveDirectoryIntegrated"

params=parse.quote_plus(connection_str)

engine=create_engine("mysql+pyodbc:///?odbc_connect=%s" % params)
connection=engine.connect()
print("OK")

connection.close()