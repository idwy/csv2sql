table_properties = {
    "ads": {
        "name": "ads",
        "columns": "(owner_id,title,category,price,city,created_at,deleted_at,id)",
        "schema": "CREATE TABLE IF NOT EXISTS ads (owner_id INTEGER(24), title TEXT, category TEXT, price INTEGER(24),"
        "city TEXT, created_at DATE, deleted_at TEXT, id INTEGER(24))",
        "csv_location": "data/ads.csv",
    },
    "users": {
        "name": "users",
        "columns": "(id, age, birthdate,city,created_at,sex,latitude,longitude,"
        "password,utm_source,utm_medium ,utm_campaign ,firstname ,"
        "lastname ,user_agent ,phone_number,connections)",
        "schema": "CREATE TABLE IF NOT EXISTS users (id INTEGER(24),age INTEGER(24),birthdate VARCHAR(25),city VARCHAR(100),"
        "created_at VARCHAR(25),sex VARCHAR(25),latitude FLOAT(25),longitude FLOAT(25),"
        "password VARCHAR(50),utm_source VARCHAR(25),utm_medium VARCHAR(25),"
        "utm_campaign VARCHAR(25),firstname VARCHAR(25),lastname VARCHAR(25),"
        "user_agent TEXT,phone_number TEXT,connections TEXT);",
        "csv_location": "data/users.csv",
    },
    "ads_transaction": {
        "name": "ads_transaction",
        "columns": "(id, ad_owner_id, buyer_user_id, ad_id, sold_price, created_at)",
        "schema": "CREATE TABLE IF NOT EXISTS ads_transaction (id INTEGER(24), ad_owner_id INTEGER(24), "
        "buyer_user_id INTEGER(24), ad_id INTEGER(24), sold_price FLOAT(25), created_at TEXT) ",
        "csv_location": "data/ads_transaction.csv",
    },
    "referrals": {
        "name": "referrals",
        "columns": "(id, referrer_user_id,referree_user_id, created_at, deleted_at)",
        "schema": "CREATE TABLE IF NOT EXISTS referrals (id INTEGER(24), referrer_user_id INTEGER(24), "
        "referree_user_id INTEGER(24), created_at TEXT, deleted_at DATE) ",
        "csv_location": "data/referrals.csv",
    },
}
