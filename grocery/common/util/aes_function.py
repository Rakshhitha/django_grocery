import json
from .encrypt_decrypt import AesCrypto

def encrypt(data, disable=False):
    """
    key to be sent "(1#p1r1xt_^%2-)yc=$6f+olxszb1xzmm_phx_#bnt&nn)j!c7"
    """
    if disable:
        return data
    else:
        aes = AesCrypto('(1#p1r1xt_^%2-)yc=$6f+olxszb1xzmm_phx_#bnt&nn)j!c7')
        encrypted_data = aes.encrypt(json.dumps(data))
        return encrypted_data

def decrypt(data, disable=False):
    """
    key to be sent "(1#p1r1xt_^%2-)yc=$6f+olxszb1xzmm_phx_#bnt&nn)j!c7"
    """
    if disable:
        return data
    else:
        aes = AesCrypto('(1#p1r1xt_^%2-)yc=$6f+olxszb1xzmm_phx_#bnt&nn)j!c7')
        decrypted_data = aes.decrypt(data)
        return json.loads(decrypted_data)


def web_encrypt(data):
    aes = AesCrypto('(1#p1r1xt_^%2-)yc=$6f+olxszb1xzmm_phx_#bnt&nn)j!c7')
    encrypted_data = aes.web_encrypt(json.dumps(data))
    return encrypted_data

