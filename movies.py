class Movie:
    def __init__(self, title, year, genre, times_played):
        self.title = title
        self.year = year
        self.genre = genre
        self.times_played = times_played

    def __str__(self):
        return f"{self.title} ({self.year})"

    def play(self):
        self.times_played += 1

class Series(Movie):
    def __init__(self, title, year, genre, episode, season, times_played):
        super().__init__(title, year, genre, times_played)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"

    def play(self):
        self.times_played += 1

pictures_list = []
breaking_bad = Series("Breaking Bad", 2008, "Drama", 1, 1, 0)
pictures_list.append(breaking_bad)
the_office = Series("The Office", 2005, "Comedy", 1, 1, 0)
pictures_list.append(the_office)
pulp_fiction = Movie("Pulp Fiction", 1994, "Crime", 0)
pictures_list.append(pulp_fiction)
the_matrix = Movie("The Matrix", 1999, "Action", 0)
pictures_list.append(the_matrix)
#coo?
#print(type(Movie) == type)

def get_movies(list):
    for item in list:
        if item == Movie:
            print(item)   
        #movie_list.append(item)
    #print(movie_list)
    #movie_by_title = sorted(movie_list, key=lambda x: x.title)
    #[print(movie) for movie in movie_by_title]


get_movies(pictures_list)