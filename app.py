from flask import Flask , jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mooc_hunter'
app.config['MONGO_URI'] = 'mongodb://saahil_ali:saahil143aasim@ds261644.mlab.com:61644/mooc_hunter'


mongo = PyMongo(app)

@app.route('/data' , methods= ['GET'])
def get_all_data() :
    data = mongo.db.data

    output = []

    for q in data.find():
            output.append({'name': q['name'] , 'price' : q['price']  , 'rating' : q['rating'] , 'certification' : q['certification'], 'Level': q['Level'], 'duration': q['duration'],'course_link':q['course_link'] })
    return jsonify({'result': output})


@app.route('/data/<name>' , methods = ['GET'])
def get_one_course(name):
    data = mongo.db.data

    output = []

    for q in data.find() :
        if name in q['name'] : output.append({'name': q['name'] , 'price' : q['price']  , 'rating' : q['rating'] , 'certification' : q['certification'], 'Level': q['Level'], 'duration': q['duration'],'course_link':q['course_link'] })


    return jsonify({'result':output})
if __name__=='__main__':
    app.run()





