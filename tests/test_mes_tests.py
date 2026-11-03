from atelier import temps_arret


def test_temps_arret_personnel():
    evenements = [
        {
            "machine": "M-01",
            "type": "ARRET",
            "code": "E42",
            "heure": "08:00:00",
            "duree": 10
        },
        {
            "machine": "M-01",
            "type": "ARRET",
            "code": "E42",
            "heure": "09:00:00",
            "duree": 15
        },
        {
            "machine": "M-02",
            "type": "ALARME",
            "code": "T01",
            "heure": "10:00:00",
            "duree": None
        },
        {
            "machine": "M-03",
            "type": "ARRET",
            "code": "E10",
            "heure": "11:00:00",
            "duree": None
        }
    ]

    resultat = temps_arret(evenements)

    assert resultat == {"M-01": 25}