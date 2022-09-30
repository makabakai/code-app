"""
马云飞
2020118092
"""

import random
import re
import string

import cherrypy
from pymongo import MongoClient

client = MongoClient()
db = client.test


class RestaurantMatcher(object):

    # Define the starting page for the search.
    @cherrypy.expose
    def index(self):
        return """
        <html>
          <head><title>Restaurant</title></head>
          <body>
          <h2>马云飞 2020118092</h2><hr>
            <h2>Search</h2>
            <h3>Type in some information :</h3>
            <form method="get" action="" target="iframe1" name="form1">
              <p>
                <span>&nbsp;&nbsp;name:&nbsp;&nbsp;&nbsp;</span>
                <input type="text" placeholder="e.g. Morris Park Bake Shop" value="" name="name" /><br><br>
                <span>borough: </span>
                <input type="text" placeholder="e.g. Bronx" value="" name="borough" /><br><br>             
                <span>&nbsp;&nbsp;street:&nbsp;&nbsp;&nbsp;</span>
                <input type="text" placeholder="e.g. Morris Park Ave" value="" name="street" /><br><br>             
                <span>&nbsp;zipcode:&nbsp;</span>
                <input type="text" placeholder="e.g. 10462" value="" name="zipcode"  /><br>
              </p>
              <button type="submit" style="margin-left:10em;" onclick="form1.action='search'">submit</button>
            </form>
            <iframe name="iframe1" ></iframe>
            <iframe name="iframe2" ></iframe><br>
            
            <h2>Insert</h2>
            <form method="get" action="" target="iframe3" name="form2">
              <p>
                <span>&nbsp;&nbsp;name:&nbsp;&nbsp;&nbsp;</span>
                <input type="text" placeholder="e.g. Morris Park Bake Shop" value="" name="name1" /><br><br>
                <span>borough: </span>
                <input type="text" placeholder="e.g. Bronx" value="" name="borough1" /><br><br>             
                <span>&nbsp;&nbsp;street:&nbsp;&nbsp;&nbsp;</span>
                <input type="text" placeholder="e.g. Morris Park Ave" value="" name="street1" /><br><br>             
                <span>&nbsp;zipcode:&nbsp;</span>
                <input type="text" placeholder="e.g. 10462" value="" name="zipcode1"  /><br><br>
                <span>building: &nbsp;</span>
                <input type="text" placeholder="e.g. Main" value="" name="building1" /><br><br>
                <span>&nbsp;&nbsp;coord: &nbsp;&nbsp;&nbsp;</span>
                <input type="text" placeholder="e.g. [0.9653, 51.8582]" value="" name="coord1" /><br><br>
                <span>&nbsp;&nbsp;cuisine: &nbsp;</span>
                <input type="text" placeholder="e.g. Deli Bar" value="" name="cuisine1" /><br>
              </p>
              <div style="float:left;"><button type="submit" style="margin-left:10em;" onclick="form2.action='insert'">insert</button></div><br>
              <div style="margin-left:4em;"><iframe name="iframe3" height="50px" frameborder="0" scrolling="no"></iframe></div>             
            </form>
          </body>
        </html>"""

    # Define the contents of iframe1; search for the restaurants and display a
    # list of them to choose from.
    @cherrypy.expose
    def search(self, name=r'.', borough=r'.', street=r'.', zipcode=r'.'):
        cursor = db.restaurants.find(
            {"name": re.compile(name.title()),
             "borough": re.compile(borough.title()),
             "address.street": re.compile(street.title()),
             "address.zipcode": re.compile(zipcode.title())})
        doc = """
            <html>
              <head></head>
              <body>
                <h3>Results</h3>
                """
        for r in cursor:
            rest_name = r['name'] if r['name'] != "" else '(No Name)'
            rest_id = r['restaurant_id']
            doc += """
               <form method="get" action="choose" target="iframe2">
                 <input type="hidden" id="restname" name="restname" value="%s">
                 <input type="hidden" id="restid" name="restid" value="%s">
                 <button type="submit">%s</button>
               </form>""" % (rest_name, rest_id, rest_name)
        doc += """
             </body>
            </html>"""
        return doc

    # Define the contents of iframe2; for a chosen restaurant, show information
    # about it.
    @cherrypy.expose
    def choose(self, restname, restid):
        cursor = db.restaurants.find({"restaurant_id": restid})
        r = next(cursor)
        rest_name = r['name']
        rest_boro = r['borough']
        rest_cuis = r['cuisine']
        rest_id = r['restaurant_id']

        doc = """<html>
          <head></head>
          <body>
            <h3>%s</h3>
            <table>
              <tr><th>Borough</th><th>Cuisine</th><th>ID</th></tr>
              <tr><td>%s</td><td>%s</td><td>%s</td></tr>
            </table>
          </body>
        </html>""" % (rest_name, rest_boro, rest_cuis, rest_id)
        return doc

    # insert a new record into the database
    @cherrypy.expose
    def insert(self, name1, borough1, street1, zipcode1, building1, coord1, cuisine1):
        rest_id = None

        # generate a unique id for the new restaurant.
        try:
            while True:
                rest_id = ''.join(random.sample(string.digits, int(8)))
                cursor = db.restaurants.find({"restaurant_id": rest_id})
                next(cursor)
        except StopIteration:
            print('unique id', rest_id)

        # transform the string into a list.
        # e.g. "[123.23, 456,45]" ==> [123.23, 456,45]
        coord1 = coord1.split(',')
        coord1 = list(float(x) for x in coord1)

        result = db.restaurants.insert_one(
            {
                "address": {
                    "building": building1,
                    "coord": coord1,
                    "street": street1,
                    "zipcode": zipcode1
                },
                "borough": borough1,
                "cuisine": cuisine1,
                "grades": [],
                "name": name1,
                "restaurant_id": rest_id
            }

        )
        return 'success,' + '  id:%s' % rest_id


if __name__ == '__main__':
    cherrypy.quickstart(RestaurantMatcher())
