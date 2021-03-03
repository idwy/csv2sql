from sqlalchemy import create_engine
import pandas as pd
from table_properties import table_properties
from constants import CHUNK_SIZE, SQL_PORT, SQL_HOST, SQL_DATABASE
import time
from command_line_parser import args
from data_normalization import hardcoded_rule_normalize, regex_rule_normalize
import logging
import ast

logging.basicConfig(level=logging.DEBUG)

# Function that inserts all df rows
def insert_all(df, table, columns, chunk_index):
    try:
        values = ",".join(map(str, [tuple(df.iloc[index].values) for index in range(df.shape[0])]))
        sql = f"INSERT INTO {table} {columns} VALUES {values};"
        sql = sql.replace("nan", "NULL")
        cursor.execute(sql)
        logging.debug(f"Inserting all rows for chunk {chunk_index}")
    except:
        logging.error(f"error inserting all row for {chunk_index}")


def connect_to_GDC():
    mysql_conn_str = f"mysql+pymysql://{args.username}:{args.password}@{SQL_HOST}:{SQL_PORT}/{SQL_DATABASE}"
    engine = create_engine(mysql_conn_str)
    cursor = engine.connect()
    return cursor


def create_table(table_schema, cursor):
    cursor.execute(table_schema)


def read_csv(file_location, index_col):
    return pd.read_csv(file_location, index_col=index_col, chunksize=CHUNK_SIZE)

def json_to_column(data, column):
    parsed_data=ast.literal_eval(data)
    if column=="phone_number":
        return parsed_data["phone_number"]
    else:
        return ','.join(str(e) for e in parsed_data["connections"])

cursor = connect_to_GDC()


# ads
logging.debug(f"Begin ads insertion")

create_table(table_properties["ads"]["schema"], cursor)
ads = read_csv(table_properties["ads"]["csv_location"], 0)

for chunk_index, chunk in enumerate(ads):
    # Data clean
    chunk["category"] = chunk["category"].apply(regex_rule_normalize)
    chunk["category"] = chunk["category"].apply(hardcoded_rule_normalize)
    insert_all(chunk, "ads", table_properties["ads"]["columns"], chunk_index)
logging.debug(f"End ads insertion\n\n")

# users
logging.debug(f"Begin users insertion")
create_table(table_properties["users"]["schema"], cursor)
users = read_csv(table_properties["users"]["csv_location"], 0)


for chunk_index, chunk in enumerate(users):
    chunk["phone_number"] = chunk["misc"].apply(lambda x : json_to_column(x,"phone_number"))
    chunk["connections"] = chunk["misc"].apply(lambda x : json_to_column(x,"connections"))
    chunk["sex"] = chunk["sex"].apply(hardcoded_rule_normalize)
    chunk = chunk.drop(columns=["misc"])
    insert_all(chunk, "users", table_properties["users"]["columns"], chunk_index)
logging.debug(f"End users insertion\n\n")


# ads_transaction
logging.debug(f"Begin ads_transaction insertion")

create_table(table_properties["ads_transaction"]["schema"], cursor)
ads_transaction = read_csv(table_properties["ads_transaction"]["csv_location"], False)

for chunk_index, chunk in enumerate(ads_transaction):
    insert_all(
               chunk,
               "ads_transaction",
               table_properties["ads_transaction"]["columns"],
               chunk_index,
               )
logging.debug(f"End ads_transaction insertion \n\n")


# referrals
logging.debug(f"Begin referrals insertion")

create_table(table_properties["referrals"]["schema"], cursor)
referrals = read_csv(table_properties["referrals"]["csv_location"], False)

for chunk_index, chunk in enumerate(referrals):
    insert_all(
               chunk, "referrals", table_properties["referrals"]["columns"], chunk_index
               )
logging.debug(f"End referrals insertion\n\n")


logging.log(logging.INFO, "Closing the connection.")
cursor.close()
