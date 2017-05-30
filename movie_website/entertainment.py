import fresh_tomatoes
import media

lock_stock = media.Movie("Lock Stock and Two Smoking Barrels",
                        "http://www.imdb.com/title/tt0120735/?ref_=nv_sr_1",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAyN2JmZmEtNjAyMy00NzYwLThmY2MtYWQ3OGNhNjExMmM4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=h6hZkvrFIj0")

in_the_loop = media.Movie("In The Loop",
                          "http://www.imdb.com/title/tt1226774/?ref_=nv_sr_1",
                          "https://upload.wikimedia.org/wikipedia/en/0/01/In_the_Loop_poster.jpg",
                          "https://www.youtube.com/watch?v=yJU2qRg5zLI")

harry_potter = media.Movie("Harry Potter film series",
                           "http://www.imdb.com/title/tt0241527/?ref_=nv_sr_2",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM0NTczMTUzOV5BMl5BanBnXkFtZTYwMzIxNTg3._V1_.jpg",
                           "https://www.youtube.com/watch?v=y6ZW7KXaXYk")

snatch = media.Movie("Snatch",
                     "http://www.imdb.com/title/tt0208092/?ref_=nv_sr_1",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA2NDYxOGYtYjU1Mi00Y2QzLTgxMTQtMWI1MGI0ZGQ5MmU4XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_SX684_AL_.jpg",
                     "https://www.youtube.com/watch?v=ni4tEtuTccc")

full_monty = media.Movie("The Full Monty",
                         "http://www.imdb.com/title/tt0119164/?ref_=fn_al_tt_1",
                         "https://upload.wikimedia.org/wikipedia/en/e/ee/TheFullMonty.UKtheatricalposter.jpg",
                         "https://www.youtube.com/watch?v=CWZBdTCsRCY")

trainspotting = media.Movie("Trainspotting",
                            "http://www.imdb.com/title/tt0117951/?ref_=nv_sr_2",
                            "https://upload.wikimedia.org/wikipedia/en/7/71/Trainspotting_ver2.jpg",
                            "https://www.youtube.com/watch?v=8LuxOYIpu-I")

movies = [in_the_loop, lock_stock, harry_potter, snatch, full_monty, trainspotting]

fresh_tomatoes.open_movies_page(movies)