from flask import Flask
from flask import jsonify
from flask import request
from oops.databasedemo.mongodb import get_db,get_product

app = Flask(__name__)


quarks = [{'name': 'up', 'charge': '+2/3'},
          {'name': 'down', 'charge': '-1/3'},
          {'name': 'charm', 'charge': '+2/3'},
          {'name': 'strange', 'charge': '-1/3'}]
# list of dictionary
productData=[]

@app.route('/hello', methods=['GET'])
def hello_world():
    print('hello called')
    db=get_db()
    data=get_product(db)
    print(data)
    for d in data:
        print(d)
        print(d['name'])
        print("productdata",productData)
        productData.append({'name':d['name']})
    return jsonify({'productDetails' : productData})
if __name__ == "__main__":
    app.run(debug=True)