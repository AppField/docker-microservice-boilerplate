import os
from json import dumps
from flask import Flask, g, Response, request
from flask_restful import Resource, Api
from neo4j import GraphDatabase, basic_auth

app = Flask(__name__)
api = Api(app)

password = os.getenv('NEO4J_PASSWORD')

driver = GraphDatabase.driver('bolt://localhost', auth=basic_auth('neo4j', password))

def get_db():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()

class Movie(Resource):
    def get(self):
        db = get_db()
        results = db.run("MATCH (")

api.add_resource(Movie, '/movies')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)