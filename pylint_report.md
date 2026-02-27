## Pylint-raportti

Pylint antaa seuraavat huomautukset koodista:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:43:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:77:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:87:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:96:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:102:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:134:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:152:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:189:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:189:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:208:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:225:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:229:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:245:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:245:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:265:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module items
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:17:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:17:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
items.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:69:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:69:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:69:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
items.py:84:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:92:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:10:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:11:0: C0103: Constant name "item_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:12:0: C0103: Constant name "comment_count" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.29/10 (previous run: 8.23/10, +0.06)
```

# Docstring-ilmoitukset

Valtaosa huomautuksia on docstring-ilmoituksia tarkoittaen, että sovelluksen moduuleissa ja funktioissa ei ole docstring-ilmoitusta selostamassa niiden toimintaa. Sovelluksessa on tehty tietoinen ratkaisu olla lisäämättä näitä dokumentointeja.

# Puuttuva palautusarvo

Raportti huomauttaa seruaavista puuttuvista palautusarvoista:
```
app.py:189:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:245:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```
Molemmat huomatukset tulevat samankaltaisista funktioista, jotka käsittelevät metodfeja `GET` ja `POST`, kuten alla kuvattuna:
```
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            flash("Tervetuloa "+username+"!")
            return redirect("/")

        flash("VIRHE: väärä tunnus tai salasana")
        return redirect("/login")

```
Teoriassa on mahdollista, että mitään `return` -komentoa ei `if` -lausekkeiden takia tulisi. Käytännössä tämä on kuitenkin mahdotonta, sillä funktio edellyttää jomman kumman metodin syöttöä.

# Vakiot eivät noudata nimeämisstandardia
Raportti antaa seuraavat ilmoitukset:
```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:10:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:11:0: C0103: Constant name "item_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:12:0: C0103: Constant name "comment_count" doesn't conform to UPPER_CASE naming style (invalid-name)
```
Käytännössä vakiot tulisi ohjeen mukaan kirjoittaa isolla. Tämä ei kuitenkaan vaikuta koodin toimivuuteen lainkaan ja vakiot nimeltään lyhyitä ja helposti havaittavissa moduulien alussa, minkä takia niihin ei tehty muutoksia.

# Vaarallinen oletusarvo
Raportti huomauttaa eräiden funktioiden oletusarvoista seuraavasti:
```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```
Ensimmäinen ilmoitus on esimerkiksi seuraavasta funktiosta:
```
def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()
```
Funktiossa parametrin oletusarvona oleva tyhjä lista aiheuttaa huomautuksen. Onglemaksi voi muodostua se, että ooetusarvo on yhteinen kaikilla funktion kutsuilla. Tällöin, jos jollakin kutsukerralla listaa muutettaisiin, näkyisi muutos kaikkien muidenkin kutsukertojen listoissa. Tässä tapauksessa koodi ei kuitenkaan muuta listaa, joten vaaraa tällaisesta ei ole.

# Liikaa argumentteja
`items.py` moduulista raportti huomauttaa joissain funktioissa olevan liikaa argumentteja:
```
items.py:17:0: R0913: Too many arguments (6/5) (too-many-arguments)
items.py:69:0: R0913: Too many arguments (6/5) (too-many-arguments)
```
Esimerkiksi ensimmäinen huomautus tulee seuraavasta funktiosta:
```
def add_item(book_name, author, grade, review, user_id, classes):
    sql = """INSERT INTO items (book_name, author, grade, review, user_id)
            VALUES (?, ?, ?, ?, ?)"""
    db.execute(sql, [book_name, author, grade, review, user_id])
```
Perusteena huomautuksessa on, että liian moni argumentti funktiossa tekee siitä vaikeamman ymmärtää. Funktion toiminta on kuitenkin melko yksinkertainen, sillä se vain lisää argumenttina olevat oliot tietokantaan. Itse koen, että tällaisessa tilanteessa on melkein parempi näyttää argumenttina olevat lisättävät oliot kuin peittää ne esimerkiksi listaan. Tässä auttaa myös selkeä funktion nimi.
