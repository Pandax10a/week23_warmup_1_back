from flask import request, Flask
import json
from dbhelpers import run_statement
from apihelpers import check_endpoint_info
import dbcreds as d

app = Flask(__name__)

@app.get('/api/gifs')
def get_restaurant():
    results = run_statement('CALL get_gifs()')
    if(type(results) == list):
        res_json = json.dumps(results, default=str)
        return res_json
    else:
        return "Sorry, there was an error getting the gifs"

# FIX ME WITH PROPER RUNNING!
if(d.production_mode == True):
    print("Running in Production Mode")
    import bjoern #type:ignore
    bjoern.run(app, "0.0.0.0", 5000)
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)