import media
import fresh_tomatoes

alpha = media.Movie("ALPHA", "Morgan Freeman , Kodi Smit-McPhee , Leonor Varela , Natassia Malthe",
                    "Aventura, Drama, Familia", "https://yifyddl.com/uploads/xcqcq8qo3UVD2lTW.png", "https://www.youtube.com/watch?v=uIxnTi4GmCo")

mile22 = media.Movie("MILE 22", "Lauren Cohan , Mark Wahlberg , Ronda Rousey , John Malkovich",
                    "Thriller , Action , Adventure , Crime", "https://yifyddl.com/uploads/qOlnIN88hLFAclPs.png", "https://www.youtube.com/watch?v=eJU6S5KOsNI")

theequalizer2 = media.Movie("THE EQUALIZER 2", "Denzel Washington , Pedro Pascal , Bill Pullman , Melissa Leo",
                    "Thriller , Crime , Action", "https://yifyddl.com/uploads/MdG91lNkW22NI6wf.png", "https://www.youtube.com/watch?v=HyNJ3UrGk_I")

themeg = media.Movie("THE MEG", "Jason Statham , Ruby Rose , Rainn Wilson , Robert Taylor",
                     "Thriller , Horror , Action , Sci-Fi", "https://yifyddl.com/uploads/t6heqJzTtW3amJQl.png", "https://www.youtube.com/watch?v=bsLk0NPRFAc")

thebombing = media.Movie("THE BOMBING", "Bruce Willis , Adrien Brody , Rumer Willis , Bingbing Fan",
                    "War , Action , Adventure , Drama", "https://yifyddl.com/uploads/obrNkDTfPNmADpbq.png", "https://www.youtube.com/watch?v=3u3cSuLJxVY")

listadeschindler = media.Movie("SCHINDLER'S LIST", "Ralph Fiennes , Liam Neeson , Embeth Davidtz , Ben Kingsley",
                    "Biography , Action , History", "https://yifyddl.com/uploads/pn5yfqF0Od3c8aZZ.png", "https://www.youtube.com/watch?v=gG22XNhtnoY")

thepianist = media.Movie("THE PIANIST", "Adrien Brody , Thomas Kretschmann , Emilia Fox , Ed Stoppard",
                    "Biography , War , Action , History , Music", "https://yifyddl.com/uploads/G8qUNaoZJjRekaV7.png", "https://www.youtube.com/watch?v=BFwGqLa_oAo")

ateoultimohomem = media.Movie("HACKSAW RIDGE", "Teresa Palmer , Luke Bracey , Sam Worthington , Hugo Weaving",
                    "History , Biography , War , Action", "https://yifyddl.com/uploads/3LrFLi7YStMbIU4v.png", "https://www.youtube.com/watch?v=s2-1hz1juBI")

gaugin = media.Movie("GAUGUIN: VOYAGE TO TAHITI", "Vincent Cassel",
                    "Biography , Romance , Drama", "https://yifyddl.com/uploads/3ZXWgQDqn1RZDKR3.png", "https://www.youtube.com/watch?v=bvQ1wZvk0EI")

lovingpablo = media.Movie("LOVING PABLO", "Penélope Cruz , Javier Bardem , Peter Sarsgaard , Colin Salmon",
                    "Biography , Crime", "https://yifyddl.com/uploads/QiC6zOmD3XefkeDB.png", "https://www.youtube.com/watch?v=Y9ni0CghN4s")

nun = media.Movie("NUN", "William McNamara",
                    "Thriller , Horror , Mystery", "https://yifyddl.com/uploads/a0i8waQ6Tjb4vHio.png", "https://www.youtube.com/watch?v=pzD9zGcUNrw")

avengers = media.Movie("AVENGERS: AGE OF ULTRON", "Scarlett Johansson , Chris Hemsworth , Chris Evans , Elizabeth Olsen",
                    "Action", "https://yifyddl.com/uploads/MVxdpxcdLZaC7Kd9.png", "https://www.youtube.com/watch?v=tmeOjFno6Do")

filmes = [alpha, mile22, theequalizer2, themeg, thebombing, listadeschindler, thepianist, ateoultimohomem, gaugin, lovingpablo, nun, avengers]

fresh_tomatoes.open_movies_page(filmes)