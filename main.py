from receiver import Receiver
from emitter import Emitter
from spy import Spy
from bomb import Bomb



from sympy import prime, factorint, mod_inverse


p, q = prime(32), prime(42)
n = p * q
print("n: %d, p: %d, q: %d" %(n, p, q))

#Phi Funktion berechnen
phi=(p-1)*(q-1)
print("phi: %d"%phi)
print("Prime Factors of Phi: ", factorint(phi))
# => Teiler von Phi

#Teilerfremde Zahl hat keine Teiler von Phi
e = 11 * 17
print("e: ",e)

#Kehrwert von e mod phi
d = mod_inverse(e, phi)
print("e%phi: ", e%phi)

#Public Key: e, n
print("Public Key e, n: ",e,n)
#Private Key d
print("Private Key d: ", d)

#Verschlüsseln:
#Nachrichtensind positive ganze Zahlen kleiner n
def crypt(k, e):
    return k ** e % n
#Klartext k:
k=23709
print("k: ",k)
#Geheimtext g:
g = crypt(k, e)
print("g: ", g)

#Entschlüsseln
k=crypt(g, d)
print("k: ", k)


if __name__ == "__main__":
    #initialize
    receiver = Receiver()
    emitter = Emitter()
    spy = Spy()
    bomb = Bomb(time_limit=100)

    #message
    receiver.define_key()
    emitter.write_message()
    emitter.encrypt_message(receiver)
    receiver.decrypt_message(emitter.encrypted_message)
    receiver.start_bomb()

    #intervention
    spy.decrypt_message_shor(emitter.encrypted_message)
    spy.stop_bomb()





