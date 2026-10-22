"""Complete checks for every validation keyword present in this frozen schema.
Standard library only; not a general-purpose Draft 2020-12 validation engine.
Fails closed for unsupported schema keywords. Does not change inputs.
"""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[3]
A=ROOT/'agents/diffusion_agent'
ALLOWED={'$schema','title','description','type','required','properties','items','additionalProperties'}
def audit(s):
    assert not set(s)-ALLOWED, 'Unsupported schema keyword'
    assert s.get('type') in {None,'object','array','string'}, 'Unsupported type'
    assert isinstance(s.get('additionalProperties',True),bool)
    for sub in s.get('properties',{}).values(): audit(sub)
    if 'items' in s: audit(s['items'])
def check(v,s,path='$'):
    types={'object':dict,'array':list,'string':str}; errors=[]
    if 'type' in s and not isinstance(v,types[s['type']]): return [path+': wrong type']
    if isinstance(v,dict):
        props=s.get('properties',{})
        errors += [path+': missing '+k for k in s.get('required',[]) if k not in v]
        if s.get('additionalProperties',True) is False: errors += [path+': extra '+k for k in v if k not in props]
        for k,sub in props.items():
            if k in v: errors += check(v[k],sub,path+'.'+k)
    if isinstance(v,list) and 'items' in s:
        for i,item in enumerate(v): errors += check(item,s['items'],path+'['+str(i)+']')
    return errors
def pairs(items):
    d={}
    for k,v in items:
        if k in d: raise ValueError('Duplicate key: '+k)
        d[k]=v
    return d
def badconstant(v): raise ValueError('Invalid JSON constant: '+v)
if __name__=='__main__':
    schema_bytes=(ROOT/'core/output_schema.json').read_bytes(); schema=json.loads(schema_bytes);audit(schema)
    report={'method':'Complete recursive checks against all validation keywords present in the unchanged course output schema; not a general-purpose Draft 2020-12 engine','schema_sha256':hashlib.sha256(schema_bytes).hexdigest(),'cases':{}}
    for case in ['primary','contrast_1']:
        raw=(A/'responses'/f'{case}_v01.json').read_bytes()
        try:
            d=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_constant=badconstant)
            errors=check(d,schema)
            nested={'agent':sorted(set(d['agent'])-{'name','specialty','version'}),'evidence':{str(i):sorted(set(e)-{'claim','source_or_reference','date_or_recency','evidence_type','notes'}) for i,e in enumerate(d['evidence']) if set(e)-{'claim','source_or_reference','date_or_recency','evidence_type','notes'}}}
            report['cases'][case]={'strict_utf8_json_parsed':True,'schema_passed':not errors,'errors':errors,'additional_top_level_fields':sorted(set(d)-set(schema['properties'])),'additional_nested_fields':nested,'evidence_entries':len(d['evidence']),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'approx_words_in_values':len(' '.join(str(v) for v in d.values()).split())}
        except Exception as e: report['cases'][case]={'strict_utf8_json_parsed':False,'schema_passed':False,'errors':[str(e)]}
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if all(v['schema_passed'] for v in report['cases'].values()) else 1)
