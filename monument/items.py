# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MonumentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    numero = scrapy.Field()
    voie = scrapy.Field()
    nom_voie = scrapy.Field()
    code_postal = scrapy.Field()
    ville = scrapy.Field()

    lat = scrapy.Field()
    lon = scrapy.Field()

    appelation = scrapy.Field()
    adresses = scrapy.Field()
    locs = scrapy.Field()
    date_protection = scrapy.Field()
    inscrit_mh = scrapy.Field()
    prec_protection = scrapy.Field()
    denomination = scrapy.Field()
    elements_mh = scrapy.Field()
    date = scrapy.Field()
    auteur = scrapy.Field()
    historique = scrapy.Field()
    statut = scrapy.Field()

    url = scrapy.Field()
