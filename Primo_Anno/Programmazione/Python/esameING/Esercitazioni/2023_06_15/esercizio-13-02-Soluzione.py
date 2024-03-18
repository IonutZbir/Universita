# Un Appointment ha una descrizione e può essere:
# - One-time (occasionale)
# - Daily (giornaliero)
# - Monthly (mensile)
# Data una data (year, month, day) e un appuntamento,
# occorre determinare se la data corrisponde all'appuntamento.

class Appointment:
    """
    Rappresenta un appuntamento. Non si dovrebbero creare istanza di questa classe.
    """

    def __init__(self, description):
        """
        Costruisce un nuovo appuntamento
        :param description: descrizione del nuovo appuntamento
        """
        self._description = description

    def occursOn(self, year, month, day):
        """
        Determina se questo appuntamento avviene in una certa data, specificata come anno, mese, giorno
        :param year: un int che rappresenta l'anno
        :param month: un int che rappresenta il mese (1..12)
        :param day: un int che rappresenta il giorno (1..31)
        :return: True se e solo se questo appuntamento avviene nella data specificata
        """
        return False


class OneTimeAppointment(Appointment):
    """
    Rappresenta un appuntamento occasionale
    """

    def __init__(self, description, year, month, day):
        """
        Costruisce un nuovo appuntamento occasionale
        :param description: la descrizione del nuovo appuntamento
        :param year: l'anno del nuovo appuntamento
        :param month: il mese del nuovo appuntamento
        :param day: il giorno del nuovo appuntamento
        """
        super().__init__(description)
        self._year = year
        self._month = month
        self._day = day

    def occursOn(self, year, month, day):
        return self._year == year and self._month == month and self._day == day


class MonthlyAppointment(Appointment):
    """
    Rappresenta un appuntamento mensile, che ricorre cioè ogni mese in un determinato giorno
    """

    def __init__(self, description, day):
        """
        Costruisce un nuovo appuntamento mensile
        :param description: la descrizione del nuovo appuntamento
        :param day: il giorno del nuovo appuntamento
        """
        super().__init__(description)
        self._day = day

    def occursOn(self, year, month, day):
        return self._day == day


class DailyAppointment(Appointment):
    """
    Rappresenta un appuntamento quotidiano
    """
    def __init__(self, description):
        super().__init__(description)

    def occursOn(self, year, month, day):
        return True


def main():
    a1 = OneTimeAppointment("Appuntamento con John", 2022, 6, 7)

    print(a1.occursOn(2022, 6, 7))
    print(a1.occursOn(2023, 6, 7))
    print(a1.occursOn(2022, 7, 7))
    print(a1.occursOn(2022, 6, 8))

    print("---")

    a2 = MonthlyAppointment("Appuntamento con lo stipendio", 1)

    print(a2.occursOn(2022, 6, 1))
    print(a2.occursOn(2022, 7, 1))
    print(a2.occursOn(2022, 6, 2))
    print(a2.occursOn(2022, 7, 2))

    print("---")

    a3 = DailyAppointment("Lavarsi i denti")
    print(a3.occursOn(2022, 6, 1))
    print(a3.occursOn(2023, 6, 1))
    print(a3.occursOn(2022, 7, 1))
    print(a3.occursOn(2022, 6, 2))


main()
