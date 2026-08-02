from parsers.charentelibre import recuperer_charentelibre
from parsers.sudouest import recuperer_sudouest

from utils import supprimer_doublons

from rss import creer_flux



def main():

    print(
        "Recherche des actualités..."
    )


    articles = []


    charente = recuperer_charentelibre()

    print(
        "Charente Libre :",
        len(charente)
    )


    articles.extend(
        charente
    )


    sudouest = recuperer_sudouest()

    print(
        "Sud Ouest :",
        len(sudouest)
    )


    articles.extend(
        sudouest
    )


    print(
        "Total avant nettoyage :",
        len(articles)
    )


    articles = supprimer_doublons(
        articles
    )


    print(
        "Après suppression doublons :",
        len(articles)
    )


    creer_flux(
        articles
    )


    print(
        "RSS généré avec succès"
    )



if __name__ == "__main__":

    main()
