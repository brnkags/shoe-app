import sqlite3

connection = sqlite3.connect("database.db")
with open('schema.sql') as s:
    connection.executescript(s.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO shoes (name, image, price) VALUES (?, ?,?)", ("Nike", "https://www.google.com/url?sa=i"
                                                                                  "&url=https%3A%2F%2Fwww.nike.com"
                                                                                  "%2Fw%2Fmens-black-shoes"
                                                                                  "-90poyznik1zy7ok&psig"
                                                                                  "=AOvVaw0cprGg2k0UsnJV_dDNKns6&ust"
                                                                                  "=1677596616018000&source=images&cd"
                                                                                  "=vfe&ved"
                                                                                  "=0CBAQjRxqFwoTCOCR0MT8tf0CFQAAAAAdAAAAABAJ", "ksh15000"))
cursor.execute("INSERT INTO shoes (name,image, price) VALUES (?, ?, ?)", ('Converse', "https://www.google.com/url?sa"
                                                                                      "=i&url=https%3A%2F"
                                                                                      "%2Fforstarsfootwear.co.ke"
                                                                                      "%2Fconverse-shoes-in-kenya"
                                                                                      "%2F346-all-star-high-top"
                                                                                      "-sneaker-black-and-white.html"
                                                                                      "&psig=AOvVaw3bfrIu4YqHYBvIV"
                                                                                      "-9QVUD1&ust=1677596766268000"
                                                                                      "&source=images&cd=vfe&ved"
                                                                                      "=0CBAQjRxqFwoTCJis9Iv9tf0CFQAAAAAdAAAAABAE", "Ksh3000"))

connection.commit()
connection.close()