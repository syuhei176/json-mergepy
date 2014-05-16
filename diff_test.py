import jsonutil


if __name__ == '__main__':
    import json
    jsondict_a={'Taro':{
    	'name' : 'Yamada',
    	'age' : 25
    },
    'Hanako':{
    	'name' : 'Takeda',
    	'age' : 22

    }}
    jsondict_b={'Taro':{
    	'name' : 'Yamada',
    	'age' : 25
    },
    'Hanako':{
    	'name' : 'Takeda',
    	'age' : 22

    },
    'Kenji':{
    	'name' : 'Kinoshita',
    	'age' : 20

    }}
    print "JSON A."
    print json.dumps(jsondict_a)
    print "JSON B."
    print json.dumps(jsondict_b)
    diff1 = jsonutil.diff(jsondict_a, jsondict_b)
    print "============="
    print "JSON Diff."
    print json.dumps(diff1)
