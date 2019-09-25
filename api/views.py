from db import Db
from flask import request
from flask_restful import Resource
from sqlalchemy import text as sql_text


class Quote(Resource):
    """ The quotes View """

    def __init__(self):
        self.db = Db()

    def get(self):
        """ Returns a list of quotes """
        query = "SELECT * FROM quote ORDER BY created DESC"
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        quotes = self.db.clean_select_results(rows, keys)

        return {
            'quotes': quotes
        }

    def post(self):
        """
        Add a quote to the db 
        Expect a JSON payload with the following format
        {
            "quote": "The quote",
            "quote_by": "The person who said the quote",
            "added_by": The person who is posting the quote"
        }
        """
        data = request.get_json()
        query = "INSERT INTO `quote` (`quote`, `quote_by`, `added_by`) VALUES (:quote, :quote_by, :added_by)"
        try:
            self.db.connection.execute(sql_text(query), data)
            return True
        except:
            return False
