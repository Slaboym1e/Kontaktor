def mserialize(val):
    return {v: getattr(val, v) for v in val.__dict__ if v!="_sa_instance_state"}

# mserialize - serialize val object
def mserialize_list(list):
    return [mserialize(m) for m in list]

def dirmserialize(val,attlist):
    return {v: getattr(val, v) for v in attlist if v != "_sa_instance_state"}

def dir_serialize_list(list,attlist):
    return [dirmserialize(m, attlist) for m in list]

def enumList(first, second):
    return [n for n, x in enumerate(first) if x[0] == second]

def enumList(first, second):
    return [n for n, x in enumerate(first) if x[0] == second]