# Kirja-arvostelut

## Soveluksen toiminnot
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen kirja-arvosteluita. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään arvosteluita.
* Käyttäjä näkee sovellukseen lisätyt arvostelut. 
* Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät arvostelut.
* Käyttäjä pystyy etsimään arvosteluita kirjan tai kirjailijan nimellä. 
* Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä kirja-arvosteluita.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät kirja-arvostelut.
* Käyttäjä pystyy valitsemaan kirjalle yhden tai useamman luokittelun (genre: dekkari, kauhu jne.; aikakausi: 2000-luku, 1950-luku jne.). Mahdolliset luokittelut ovat tietokannassa.
* Pääasiallinen tietokohde on arvostelu ja toissijainen tietokohde kommentti.


## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```

