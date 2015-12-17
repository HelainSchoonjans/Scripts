#!/usr/bin/python
# - * -coding: utf - 8 - * -

import os

from pyes import *

test_indexes = ["test-index1"]

conn = ES(os.environ['ES_URL'])

def delete_index(index_name):
    try:
        conn.indices.delete_index(index_name)
    except:
        pass

def create_index(index_name, settings=None):
    conn.indices.create_index(index_name, settings)
	
def recreate_index(index_name, settings=None):
	delete_index(index_name)
	create_index(index_name, settings)

settings={
    'settings': {
        'analysis': {
            'filter'  : {
                'nGram_filter': {
                    'type'       : 'nGram',
                    'min_gram'   : 1,
                    'max_gram'   : 10,
                    'token_chars': {
                        'letter',
                        'digit',
                        'punctuation',
                        'symbol'
                    }
                }
            },
            'analyzer': {
                'nGram_analyzer'     : {
                    'type'     : 'custom',
                    'tokenizer': 'whitespace',
                    'filter'   : {
                        'lowercase',
                        'asciifolding',
                        'nGram_filter'
                    }
                },
                'whitespace_analyzer': {
                    'type'     : 'custom',
                    'tokenizer': 'whitespace',
                    'filter'   : {
                        'lowercase',
                        'asciifolding'
                    }
                }
            }
        }
    }
}

boolean = {
    'type': 'boolean'
}

long = {
    'type': 'long'
}

double = {
    'type': 'double'
}

date = {
    'type': 'date',
    'format': 'dateOptionalTime'
}

deeply_analyzed = {
    'type': 'string',
    'index_analyzer' : 'nGram_analyzer',
    'search_analyzer': 'whitespace_analyzer'
}

multi_field = {
    'type': 'string',
    'index': 'not_analyzed',
    'fields': {
        'analyzed': {
            'type': 'string',
            'index_analyzer' : 'nGram_analyzer',
            'search_analyzer': 'whitespace_analyzer'
        }
    }
}

inserts = {
    'type': 'long',
    'index_name': 'insert'
}

dynamic_templates = [
    {
        'str': {
            'match':                  '*',
            'match_mapping_type':     'string',
            'mapping':                multi_field
        }
    }
]

mappings = {
    'X': {
        '_all': {
            'enabled': False
        },
        'dynamic_templates': dynamic_templates,
        'properties': {
            
        }
    }
}

for index in test_indexes:
    recreate_index(index, settings)
for mapping in mappings:
    conn.indices.put_mapping(mapping, mappings.get(mapping), test_indexes)

print("Elastic setup successful.")
