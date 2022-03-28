import sqlite3
import pandas as pd


def get_frame_from_sqlite(sqlitedb, tablename):
    # Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect(sqlitedb)
    df = pd.read_sql_query(f"SELECT * from {tablename}", con)
    con.close()
    return df


def get_frame(fname: str, tablename=None):
    if fname.endswith('.csv'):
        df = pd.read_csv(fname)
    elif fname.endswith('.db'):
        if tablename is None:
            raise AttributeError('You must provide table name if you read a data from database')
        else:
            df = get_frame_from_sqlite(fname, tablename)
    else:
        raise AttributeError('Given file type not recognized')

    return df
