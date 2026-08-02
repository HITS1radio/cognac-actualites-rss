import requests
import xml.etree.ElementTree as ET

from utils import nettoyer_texte


URL = "https://www.ici.fr/auvergne-rhone-alpes/ardeche-07"


def recuperer_charentelibre():

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
                    "source": "Charente Libre",
                    "type": "Actualité"
                }
            )


    except Exception as erreur:

        print(
            "Erreur Charente Libre :",
            erreur
        )


    return articles
