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


## Sovelluksen toiminta suurella tietomäärällä
Suuri määrä testidataa luotiin `seed.py` tiedoston avulla. 
Käytännössä se luo:
* tuhat käyttäjää
* sata tuhatta arvostelua
* miljoona kommenttia
Eniten raitusta tämä tuottaa etusivulle, joka pyrkii näyttämään kaikki 100 000 arvostelua kerralla. Yrittäessä käynnistää sovellusta ilman toimenpiteitä etusivu ei ladannut käytännössä ollenkaan. Sivun latausta saatiin nopeutettua huomattavasti lisäämällä siihen sivutus, jossa etusivu näyttää kymmenen arvostelua kerralla. Ideana on, että arvostelut näytetään dynaamisesti, eli ne ladataan aina erikseen käyttäjän klikatessa seruaavan sivun. Etusivun lataus kestää sivutuksella avitettuna silti noin 5 s, mikä on käyttökokemusta olennaisesti. Alla neljän ensimmäisen sivun läpi selaaminen pelkällä sivutuksella:
```
elapsed time: 5.03 s
127.0.0.1 - - [26/Feb/2026 15:13:22] "GET / HTTP/1.1" 200 -
elapsed time: 0.03 s
127.0.0.1 - - [26/Feb/2026 15:13:22] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 5.11 s
127.0.0.1 - - [26/Feb/2026 15:13:49] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [26/Feb/2026 15:13:49] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 4.69 s
127.0.0.1 - - [26/Feb/2026 15:13:56] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [26/Feb/2026 15:13:56] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 5.11 s
127.0.0.1 - - [26/Feb/2026 15:14:05] "GET /4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [26/Feb/2026 15:14:05] "GET /static/main.css HTTP/1.1" 304 -
```
Ongelma juontuu siitä, että kommenttien lukumäärän selvitys pelkän arvostelun pohjalta on vaikeaa ja täten hidasta. Tätä nopeutettiin lisäämällä skeemaan indeksointi:
`CREATE INDEX idx_item_comments ON comments (item_id);`
Tällöin sivujen vaihto saatiin nopeutettua sekunnin sadasosien tasolle:
```
elapsed time: 0.01 s
127.0.0.1 - - [26/Feb/2026 15:21:08] "GET /1 HTTP/1.1" 200 -
elapsed time: 0.02 s
127.0.0.1 - - [26/Feb/2026 15:21:08] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [26/Feb/2026 15:21:21] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [26/Feb/2026 15:21:21] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [26/Feb/2026 15:21:22] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [26/Feb/2026 15:21:22] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.01 s
127.0.0.1 - - [26/Feb/2026 15:21:23] "GET /4 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [26/Feb/2026 15:21:23] "GET /static/main.css HTTP/1.1" 304 -
```

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

Asennuksen mukana on tiedosto `seed.py`, jonka ajamalla voit luoda ison määrän testidataa sovelluksen testaamiseen (kts. "Sovelluksen toiminta suurella tietomäärällä").
