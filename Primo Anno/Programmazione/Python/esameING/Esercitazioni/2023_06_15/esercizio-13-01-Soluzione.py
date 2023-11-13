# Realizzare una classe che rappresenti un cerchio identificato dal
# suo centro (a sua volta modellato dalla classe Punto) e dal suo raggio.
# La classe deve permettere di calcolare l'area e il perimetro del cerchio,
# e determinare se due cerchi si sovrappongono.

from math import pi, dist


class Cerchio:
    def __init__(self, centro, raggio):
        self._centro = centro
        self._raggio = raggio

    def area(self):
        return pi * self._raggio ** 2

    def perimetro(self):
        return 2 * pi * self._raggio

    def centro(self):
        return self._centro

    def raggio(self):
        return self._raggio

    def sovrapposto_a(self, altro_cerchio):
        return self._centro.distanza(altro_cerchio.centro()) < self._raggio + altro_cerchio.raggio()

    def __repr__(self):
        return "Cerchio{centro = %s, raggio = %.2f}" % (self._centro, self._raggio)


class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def distanza(self, altro_punto):
        return dist([self._x, self._y], [altro_punto.x(), altro_punto.y()])

    def __repr__(self):
        return "Punto{x = %.2f, y  = %.2f}" % (self._x, self._y)


c1 = Cerchio(Punto(0.0, 0.0), 1.0)

print(c1, "area = ", c1.area())
print(c1, "perimetro = ", c1.perimetro())

c2 = Cerchio(Punto(1.5, 0.0), 1.0)
print(c1, "si sovrappone a", c2, c1.sovrapposto_a(c2))

c3 = Cerchio(Punto(2.1, 0.0), 1.0)
print(c1, "si sovrappone a", c3, c1.sovrapposto_a(c3))

c4 = Cerchio(Punto(-2.1, 0.0), 1.1)
print(c1, "si sovrappone a", c4, c1.sovrapposto_a(c4))
