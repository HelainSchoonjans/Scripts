# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:03:38 2016

@author: hschoonjans
"""

from html.parser import HTMLParser
                
class MyWargameHTMLParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.reachedTitle = False      
        
        self.current_technology_name = ''
        self.required_technologies = []
        self.rows = {}
    
    def handle_starttag(self, tag, attrs):
        if self.reachedTitle:
            if tag == "a":
                technology_titles = [attr[1] for attr in attrs if attr[0] == "title" and attr[1] and attr[1] != "Détail" and attr[1] != "Créer" and not("sur le même territoire" in attr[1])]
                if technology_titles:
                    self.required_technologies.append(technology_titles[0])
                if [attr for attr in attrs if attr[0] == "title" and attr[1] == "Détail"]:
                    self.current_technology_name = "Détail"
                    self.required_technologies = []
    
    def handle_endtag(self, tag):
        if self.reachedTitle:
            if tag == "tr" and self.current_technology_name:
                self.rows[self.current_technology_name] = list(set(self.required_technologies))
    
    def handle_data(self, data):
        if data == "Val.":
            self.reachedTitle = True
        if self.current_technology_name == "Détail":
            print(data)
            self.current_technology_name = data
        
import os.path

output_file_path = '../../../data/technologies.json'
if not os.path.exists(output_file_path):
    html_file_location = '../../../data/Création - Ragnarok War Game.htm'
    html_contents = open(html_file_location, 'r', encoding="utf-8").read()
    
    parser = MyWargameHTMLParser()
    parser.feed(html_contents)
    

    import json
    with open(output_file_path, 'w') as outfile:
        json.dump(parser.rows, outfile)
        
import json
with open(output_file_path, 'r') as inputfile:
    technology_and_requirements = json.loads(inputfile.read())
    print(technology_and_requirements)
    
    import networkx as nx
    
    graph = nx.DiGraph()
    
    for technology, requirements in technology_and_requirements.items():
        for requirement in requirements:
            graph.add_edge(requirement, technology)
    
    import matplotlib.pyplot as plt
    nx.draw(graph)
    plt.show()
    plt.savefig("../../../data/technology_graph.pdf")
    


