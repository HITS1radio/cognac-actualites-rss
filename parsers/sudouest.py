import requests
import xml.etree.ElementTree as ET

from utils import nettoyer_texte


URL = "https://www.ledauphine.com/ardeche/rss"


def recuperer_sudouest():

    articles = []

    try:

        reponse = requests.get(
            URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        reponse.raise_for_status()


        racine = ET.fromstring(
            reponse.content
        )


        for item in racine.findall(
            ".//item"
        ):

            titre = item.findtext(
                "title",
                ""
            )

            lien = item.findtext(
                "link",
                ""
            )

            description = item.findtext(
                "description",
                ""
            )


            if not titre or not lien:
                continue


            articles.append(
                {
                    "title": nettoyer_texte(titre),
                    "url": lien,
                    "description": nettoyer_texte(description),
                    "source": "Sud Ouest",
                    "type": "Actualité"
                }
            )


    except Exception as erreur:

        print(
            "Erreur Sud Ouest :",
            erreur
        )


    return articles
