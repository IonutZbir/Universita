def converti_data(data):
    """
    Converte una stringa dal formato gg/mm/aaaa al formato aaaa/mm/gg

    :param data: data in formato gg/mm/aaaa
    :type data: str
    :return: data in formato aaaa/mm/gg
    :rtype: str
    """
    componenti_data = data.split("/")
    componenti_data.reverse()
    return "/".join(componenti_data)


def main():
    print(converti_data("20/04/2023"))


main()
