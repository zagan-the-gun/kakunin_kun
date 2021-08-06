from flask import Flask, render_template
from flask import request
import geoip2.database

app = Flask(__name__)

@app.route("/", methods=['GET'])
def top():
    return '<a href="./kakunin_kun">kakunin_kun</a>'

@app.route("/kakunin_kun", methods=['GET'])
def kakunin_kun():
    if request.headers.getlist("X-Forwarded-For"):
        GIP=request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    else:
        GIP=request.environ['REMOTE_ADDR']

    for h in request.headers:
        print(h)

    reader = geoip2.database.Reader('./static/GeoLite2-City.mmdb')
    response = reader.city(GIP)

    profile = {
                'gip':GIP,
                'country_code'    : response.country.iso_code,
                'state_name'      : response.subdivisions.most_specific.name,
                'city_name'       : response.city.name,
                'postal_code'     : response.postal.code,
                'User-Agent'      : request.headers.get('User-Agent'),
                'Accept'          : request.headers.get('Accept'),
                'Referer'         : request.headers.get('Referer'),
                'Accept-Language' : request.headers.get('Accept-Language'),
              }
    print(profile)

    renderpage = render_template("kakunin_kun.html", profile=profile)
    return renderpage

