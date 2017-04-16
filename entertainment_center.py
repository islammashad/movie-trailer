import fresh_tomatoes
import media


"""This section is used to initialize the values
in the Movie Class in the Media Module for each movie"""

# Toy Story Movie
toy_pic = "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
toy_story = media.Movie("Toy Story",
                        "story of a boy and his toys",
                        toy_pic,
                        "https://www.youtube.com/\
                        watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/"
                     "wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY") 
# jurassic park Movie
jurassic_park = media.Movie("Jurassic park",
                            "An Adventure 65 Million Years in Tte Making",
                            "https://upload.wikimedia.org/"
                            "wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                            "https://www.youtube.com/watch?v=_IesovZQR4g")
# The Matrix Movie
matrix = media.Movie("Matrix",
                     "Very amazing Movie with science fiction ",
                     "https://www.movieposter.com/"
                     "posters/archive/main/9/A70-4902",
                     "https://www.youtube.com/\
                     watch?v=m8e-FF8MsqU")
# Mad Max Movie
mad_max_fury_road = media.Movie("Mad Max Fury Road",
                                "In a stark desert landscape \
                                where humanity is broken",
                                "https://encrypted-tbn3.gstatic.com/\
                                images?q=tbn:ANd9GcSY9szIPbtk1-\
                                hwxdEVRJIHT_pgYGNnFkFSWsCjlKFGP3Pu77Oo",
                                "https://www.youtube.com/watch?v=YWNWi-ZWL3c")
# Whiplash Movie
whiplash = media.Movie("Whiplash",
                       "young drummer enrolls",
                       "https://encrypted-tbn3.gstatic.com/\
                       images?q=tbn:ANd9GcSyLORvKKvCi7-\
                       vy8vwi2s8F62aG7D36H15A8rOVfP2d7koyA9I",
                       "https://www.youtube.com/\
                       watch?v=tYkuvB2f5XU")
# Pass list into website generator
movies = [toy_story, avatar, jurassic_park,
          matrix, mad_max_fury_road, whiplash
          ]
# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)
