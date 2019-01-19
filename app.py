from flask import Flask , jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mooc_hunter'
app.config['MONGO_URI'] = 'mongodb://saahil_ali:saahil143aasim@ds261644.mlab.com:61644/mooc_hunter'


mongo = PyMongo(app)

@app.route('/udacityData' , methods= ['GET'])
def get_all_data() :
    udacityData = mongo.db.udacityData

    output = []

    for q in udacityData.find():
        output.append({'name': q['name'] , 'provider' : q['provider']})
    return jsonify({'result':output})

if __name__=='__main__':
    app.run(debug=True)