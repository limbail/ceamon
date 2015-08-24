from django.db import models as m
from django.core.urlresolvers import reverse
from os import urandom
from base64 import b64encode, b64decode
from Crypto.Cipher import ARC4
from django.conf import settings

def get_value(name):
    def f(self):
        return locker.decrypt(getattr(self, 'e_%s'%name))
    return f

def set_value(name):
    def f(self, value):
        setattr(self, 'e_%s'%name, locker.encrypt(value))
    return f

class locker(m.Model):
    SALT_SIZE = 8

    title = m.CharField(max_length=128)
    e_username = m.TextField(blank=True)
    e_password = m.TextField(blank=True)
    e_url = m.TextField(blank=True)
    e_notes = m.TextField(blank=True)

    @staticmethod
    def encrypt(plaintext):
        salt = urandom(locker.SALT_SIZE)
        arc4 = ARC4.new(salt + settings.SECRET_KEY)
        plaintext = "%3d%s%s" % (len(plaintext), plaintext, urandom(256-len(plaintext)))
        return "%s$%s" % (b64encode(salt), b64encode(arc4.encrypt(plaintext)))

    @staticmethod
    def decrypt(ciphertext):
        salt, ciphertext = map(b64decode, ciphertext.split('$'))
        arc4 = ARC4.new(salt + settings.SECRET_KEY)
        plaintext = arc4.decrypt(ciphertext)
        return plaintext[3:3+int(plaintext[:3].strip())]

    def encrypted_property(name):
        return property(get_value(name), set_value(name))

    username = encrypted_property('username')
    password = encrypted_property('password')
    url = encrypted_property('url')
    notes = encrypted_property('notes')
