from cmath import e
from crypt import methods
from errno import EL
from flask import *
from unidecode import unidecode


app=Flask(__name__)


@app.route("/code" , methods=["GET","POST"])
def uni():
    x = unidecode(request.json['data'])
    return json.dumps({"status_code":200,"data":x})




@app.route("/admin/login", methods=["GET","POST"])
def login():
    try:
        if request.json["user"] == "shahab" and request.json["password"] == 123:
            d = {"status_code":200,
                 "MSG":"login successfully"}
            return json.dumps(d)
        else:
            d = {"status_code":401,
                    "MSG":"user or pass wrong"}
            return json.dumps(d)
    except Exception as e:
        ee={"status_code":400,
            "msg":str(e)}

app.run()

