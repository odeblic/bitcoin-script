from bitcoin import *

priv_key = sha256('this is the seed of your wallet')

pub_key = privtopub(priv_key)

addr = pubtoaddr(pub_key)

inputs = history(addr)

outputs = [{'value': 10000, 'address': '1xxxxxx_receiver_of_funds_xxxxxxxx'}]

tx1 = mktx(inputs, outputs)

tx2 = sign(tx1, 0, priv_key)

tx3 = sign(tx2, 1, priv_key)

pushtx(tx3)

