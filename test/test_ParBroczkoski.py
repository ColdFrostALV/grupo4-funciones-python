#Número par
#funciones/es_par.py
def es_par(n):
 """Devuelve True si el número es par, False si es impar."""
 return n % 2 == 0
#tests/test_es_par.py
from funciones.es_par import es_par
def test_es_par():
assert es_par(4) is True
 assert es_par(7) is False