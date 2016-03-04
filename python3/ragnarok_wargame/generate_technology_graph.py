# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:03:38 2016

@author: hschoonjans
"""

from html.parser import HTMLParser

class MyWargameHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inRow = False
        self.inColumn = False
        self.reachedTitle = False
        self.row_contents = []
        self.rows = []
    
    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            #print("Encountered a start tag:", tag)
            self.inRow = True
            #print(attrs)
        elif tag == "td":
            self.inColumn = True
            
    def handle_endtag(self, tag):
        if self.reachedTitle:
            if tag == "tr":
                #print("Encountered an end tag :", tag)
                self.inRow = False
                import re
                data = ";".join(self.row_contents)
                # remove the number of unit possessed
                data = re.sub(r'\(;#[0-9];\);', '', data)
                # remove the parenthesis arount the second military value.
                data = re.sub(r'\(;|;\);', '', data)
                if(data):
                    print(data)
                    #print(len(data.split(";")))
                    self.rows.append(data)
                self.row_contents =[]
            elif tag == "td":
                self.inColumn = False
            
    def handle_data(self, data):
        if data == "Val.":
            self.reachedTitle = True
            self.row_contents.append("Nombre")
            self.row_contents.append("Nom")
        if self.reachedTitle: 
            if self.inColumn:
                self.row_contents.append(data)
                #print("Encountered some data  :", data)

class Technology:
    def __init__(self, comma_separated_data):
        #Nombre;Nom;Val.;Mil.;CP;CoÃ»t;Dricks;CoÃ»t;UnitÃ©s;
        #CoÃ»t;Res1;CoÃ»t;Res2;CoÃ»t;Res3;CoÃ»t;Res4;UnitÃ©s;
        #requise;Technologie;requise;ou;ou;ou;Formation;TC

        data = comma_separated_data.split(";")
        self.number = data[0]
        self.name = data[1]
        #self.x = data[2]
        self.military_value = data[3:4]
        self.cp = data[5]
        #self.drick_cost = data[5:6]
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
        
        
html_file_location = '../../../data/Création - Ragnarok War Game.htm'
html_contents = open(html_file_location, 'r', encoding="utf-8").read()

parser = MyWargameHTMLParser()
parser.feed(html_contents)

# I should really  find a way to transform the number of units into tuples, and find the empty spaces...

technologies = []
for row in parser.rows:
    technologies.append(Technology(row).to_JSON())

import json
with open('../../../data/technologies.json', 'w') as outfile:
    json.dump(technologies, outfile)

