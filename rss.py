from feedgen.feed import FeedGenerator
import html

from utils import date_rss


def creer_flux(articles):

    fg = FeedGenerator()


    fg.title(
        "Actualités Cognac"
    )


    fg.link(
        href="https://hits1radio.github.io/cognac-actualites-rss/rss.xml"
    )


    fg.description(
        "Actualités locales de Cognac - Charente Libre et Sud Ouest"
    )


    for article in articles[:100]:

        item = fg.add_entry()


        item.title(
            html.escape(
                article["title"]
            )
        )


        item.link(
            href=article["url"]
        )


        description = f"""
        <p>
        <strong>{html.escape(article['title'])}</strong>
        </p>

        <p>
        📰 {html.escape(article['source'])}
        </p>

        <p>
        {html.escape(article['description'])}
        </p>
        """


        item.description(
            description
        )


        item.pubDate(
            date_rss()
        )


        item.guid(
            article["url"]
        )


    fg.rss_file(
        "rss.xml"
    )
