from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
import geopandas as gpd
from shapely.geometry import Point, Polygon
import geojson
import tempfile


app = Flask(__name__)


@app.route('/', methods= ['GET', 'POST'])
def geo():
    return render_template('index.html')

@app.route('/postmethod', methods=['GET','POST'])
def postmethod():
    latitude = request.args.get('lat', 0, type=float)
    longitude = request.args.get('lng', 0, type=float)
    gdf = gpd.read_file('FCC Ward ShapleFile/Western_Area_Urban_Wards.shp')
    pnt = Point(longitude, latitude)
    ward_exists = False
    for i in range(48):
        if gdf.loc[i, 'geometry'].contains(pnt):
            ward_exists = True
            ident = i
    if ward_exists == True:
        ward = int((gdf.loc[ident, 'Ward_No']))
        id = ward-399
        json_file = gdf.loc[id,'geometry'].__geo_interface__
        send_file = {"type": "Feature",
         "geometry": json_file,
        "ward":str(ward)
                     }
        ward = str(ward)
        return jsonify(result = send_file)
    else:
        return jsonify(result = 'Nothing')


#


# if __name__ == '__main__':
#     app.run(host='localhost', port=80,debug=True)
