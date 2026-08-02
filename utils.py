import hashlib
from datetime import datetime, timezone


def nettoyer_texte(texte):

    if not texte:
        return ""

    return (
        texte
        .replace("\n", " ")
        .replace("\t", " ")
        .strip()
    )


def creer_id(titre, url):

    valeur = titre + url

    return hashlib.md5(
        valeur.encode("utf-8")
    ).hexdigest()



def supprimer_doublons(articles):

    resultat = []

    vus = set()


    for article in articles:

        identifiant = creer_id(
            article["title"],
            article["url"]
        )


        if identifiant in vus:
            continue


        vus.add(
            identifiant
        )

        resultat.append(
            article
        )


    return resultat



def date_rss():

    return datetime.now(
        timezone.utc
    )
