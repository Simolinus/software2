import json
import mariadb
from flask import Flask, Response

app = Flask(__name__)

connection = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    user="user",
    password="password",
    database="airports",
    autocommit=True,
)


@app.route("/prime_number/<int:int_num>")
def calculate_sum(int_num):
    try:
        if int_num > 1:
            is_prime = True
            for num in range(2, int_num):
                if int_num % num == 0:
                    is_prime = False
                    break
        else:
            is_prime = False
        response = {
            "Number": int_num,
            "isPrime": is_prime,
        }
        return response

    except ValueError:
        response = {"message": "Invalid number as addend"}
        json_response = json.dumps(response)
        http_response = Response(
            response=json_response, status=400, mimetype="application/json"
        )
        return http_response


@app.route("/airport/<icao>")
def airport_by_icao(icao):
    try:
        sql = "SELECT name, municipality FROM airport WHERE ident = ?"
        cursor = connection.cursor()
        cursor.execute(sql, (icao,))
        result = cursor.fetchone()
        cursor.close()
        if result == None:
            response = {"message": "Invalid icao"}
            return response
        else:
            name = result[0]
            municipality = result[1]
            response = {
                "ICAO": icao,
                "Name": name,
                "Location": municipality,
            }
            return response

    except ValueError:
        response = {"message": "Invalid number as addend"}
        json_response = json.dumps(response)
        http_response = Response(
            response=json_response, status=400, mimetype="application/json"
        )
        return http_response


@app.errorhandler(404)
def page_not_found(error_code):
    response = {"message": "Invalid endpoint"}
    json_response = json.dumps(response)
    http_response = Response(
        response=json_response, status=404, mimetype="application/json"
    )
    return http_response


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=5000)
