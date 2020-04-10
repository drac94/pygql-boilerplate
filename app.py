#! usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from src.graphql.schema import schema
from src.datastore.db_store import get_session

app = Flask(__name__)
CORS(app)
app.debug = True

session = get_session()

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True, context={"session": session}
    ),
)


@app.route("/")
def index():
    return "Go to /graphql"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
