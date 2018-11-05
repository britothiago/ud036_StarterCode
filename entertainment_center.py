import media
import fresh_tomatoes

alpha_lista = "Morgan Freeman, Kodi Smit-McPhee, Leonor Varela,"\
                "Natassia Malthe, Aventura, Drama, Familia"
alpha = media.Movie("ALPHA",
                    alpha_lista,
                    "Action, Crime",
                    "https://yifyddl.com/uploads/xcqcq8qo3UVD2lTW.png",
                    "https://www.youtube.com/watch?v=uIxnTi4GmCo")

mile22_lista = "Lauren Cohan, Mark Wahlberg, Ronda Rousey,"\
                "John Malkovich, Thriller, Action, Adventure , Crime"

mile22 = media.Movie("MILE 22",
                     mile22_lista,
                     "Action, Crime",
                     "https://yifyddl.com/uploads/qOlnIN88hLFAclPs.png",
                     "https://www.youtube.com/watch?v=eJU6S5KOsNI")

theequalizer2_lista = "Denzel Washington, Pedro Pascal,"\
                        "Bill Pullman, Melissa Leo"
theequalizer2 = media.Movie("THE EQUALIZER 2",
                            theequalizer2_lista,
                            "Thriller, Crime, Action",
                            "https://yifyddl.com/uploads/MdG91lNkW22NI6wf.png",
                            "https://www.youtube.com/watch?v=HyNJ3UrGk_I")

themeg_lista = "Jason Statham, Ruby Rose,"\
               "Rainn Wilson, Robert Taylor"
themeg = media.Movie("THE MEG",
                     themeg_lista,
                     "Thriller, Horror, Action, Sci-Fi",
                     "https://yifyddl.com/uploads/t6heqJzTtW3amJQl.png",
                     "https://www.youtube.com/watch?v=bsLk0NPRFAc")

thebombing_lista = "Bruce Willis, Adrien Brody,"\
                    "Rumer Willis, Bingbing Fan"
thebombing = media.Movie("THE BOMBING",
                         thebombing_lista,
                         "War, Action, Adventure, Drama",
                         "https://yifyddl.com/uploads/obrNkDTfPNmADpbq.png",
                         "https://www.youtube.com/watch?v=3u3cSuLJxVY")

listadeschindler_lista = "Ralph Fiennes, Liam Neeson,"\
                            "Embeth Davidtz, Ben Kingsley"
listadeschindler_poster = "https://yifyddl.com/uploads/"\
                            "pn5yfqF0Od3c8aZZ.png"
listadeschindler = media.Movie("SCHINDLER'S LIST",
                               listadeschindler_lista,
                               "Biography, Action, History",
                               listadeschindler_poster,
                               "https://www.youtube.com/watch?v=gG22XNhtnoY")

thepianist_lista = "Adrien Brody, Thomas Kretschmann,"\
                    "Emilia Fox, Ed Stoppard"
thepianist = media.Movie("THE PIANIST",
                         thepianist_lista,
                         "Biography, War, Action, History, Music",
                         "https://yifyddl.com/uploads/G8qUNaoZJjRekaV7.png",
                         "https://www.youtube.com/watch?v=BFwGqLa_oAo")

ateoultimohomem_lista = "Teresa Palmer, Luke Bracey,"\
                            "Sam Worthington, Hugo Weaving"
ateoultimohomem_poster = "https://yifyddl.com/uploads/"\
                            "3LrFLi7YStMbIU4v.png"
ateoultimohomem = media.Movie("HACKSAW RIDGE",
                              ateoultimohomem_lista,
                              "History, Biography, War, Action",
                              ateoultimohomem_poster,
                              "https://www.youtube.com/watch?v=s2-1hz1juBI")

gaugin = media.Movie("GAUGUIN",
                     "Vincent Cassel",
                     "Biography, Romance, Drama",
                     "https://yifyddl.com/uploads/3ZXWgQDqn1RZDKR3.png",
                     "https://www.youtube.com/watch?v=bvQ1wZvk0EI")

lovingpablo_lista = "Penelope Cruz, Javier Bardem,"\
                    "Peter Sarsgaard, Colin Salmon"
lovingpablo_poster = "https://yifyddl.com/uploads/"\
                        "QiC6zOmD3XefkeDB.png"
lovingpablo = media.Movie("LOVING PABLO",
                          lovingpablo_lista,
                          "Biography, Crime",
                          lovingpablo_poster,
                          "https://www.youtube.com/watch?v=Y9ni0CghN4s")

nun = media.Movie("NUN",
                  "William McNamara",
                  "Thriller, Horror, Mystery",
                  "https://yifyddl.com/uploads/a0i8waQ6Tjb4vHio.png",
                  "https://www.youtube.com/watch?v=pzD9zGcUNrw")

avengers_lista = "Scarlett Johansson, Chris Hemsworth,"\
                    "Chris Evans, Elizabeth Olsen"
avengers = media.Movie("AVENGERS",
                       avengers_lista,
                       "Action",
                       "https://yifyddl.com/uploads/MVxdpxcdLZaC7Kd9.png",
                       "https://www.youtube.com/watch?v=tmeOjFno6Do")


lista_filmes = [alpha, mile22, theequalizer2, themeg,\
                thebombing, thepianist,\
                ateoultimohomem, gaugin, listadeschindler,\
                nun, avengers, lovingpablo]
filmes = lista_filmes

'#Chamando a função para a criação do html'
fresh_tomatoes.open_movies_page(filmes)
