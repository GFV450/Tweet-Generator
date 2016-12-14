import httplib2
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hey you out there in the cold \n Getting lonely getting old \n Can you feel me? \n Hey you standing in the aisles \n With itchy feet and fading smiles \n Can you feel me? \n Hey you don't help them to bury the light \n Don't give in without a fight"

if __name__ == "__main__":
    app.run()
