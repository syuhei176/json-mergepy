import jsonutil


if __name__ == '__main__':
    import json
    jsondiff={}


    jsondict_base={'a':
                   {'b':{
                         'array':[{'x':0,'y':5}]
                         },
                    'c':{
                         'text':'aaa',
                         'bool':True,
                         'num':5
    }}}
    jsondict_a={'a':
                   {'b':{
                         'array':[{'x':0,'y':5}],
                         'bool':True
                         },
                    'c':{
                         'text':'aaa',
                         'bool':True,
                         'num':5
    }}}
    jsondict_b={'a':
                   {'b':{
                         'array':[{'x':0,'y':5}]
                         },
                    'c':{
                         'text':'aaa',
                         'bool':True
    }}}
    print "base JSON."
    print json.dumps(jsondict_base)
    print "derivation A."
    print json.dumps(jsondict_a)
    print "derivation B."
    print json.dumps(jsondict_b)
    jsondiff = jsonutil.merge(jsondict_a, jsondict_b, jsondict_base)
    print "============="
    print "merge result."
    print json.dumps(jsondiff)
