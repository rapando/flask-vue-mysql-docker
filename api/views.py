from db import Db
from flask import request
from flask_restful import Resource
from sqlalchemy import text as sql_text
from sympy import *

class Equacao(Resource):
    """ A view de equacao """

    def __init__(self):
        self.db = Db()

    def get(self):
        """ Retorna a lista de areas """
        query = "SELECT * FROM area ORDER BY created DESC"
        res = self.db.connection.execute(query)
        rows = res.fetchall()
        keys = res.keys()
        areas = self.db.clean_select_results(rows, keys)

        return {
            'area': areas
        }

    def post(self):
        """
        Adiciona a area calculada no db
        JSON payload vai vir assim
        {
            "perimetro": numero
        }
        """
        data = request.get_json()
        print(type(data))

        x, y = symbols('x y')

        derivada = diff(data.perimetro*x - 2*x**2)

        lado = solveset(Eq(derivada, 0), x)

        area = (data.perimetro - lado._sup*2) * lado._sup
        query = "INSERT INTO `equacao` (`area`) VALUES (:area)"
        try:
            self.db.connection.execute(sql_text(query), area)
            return True
        except:
            return False
