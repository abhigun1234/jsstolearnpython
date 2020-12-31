def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.MyRetail
    return db


def add_product(db):
    db.product.insert({"name": "addidas","price":123})


def get_product(db):
    return db.product.find()


if __name__ == "__main__":
    db = get_db()
    add_product(db)
    print(get_product(db))
