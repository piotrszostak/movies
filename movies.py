class Movie:
    def __init__(self, title, year, genre, times_played):
        self.title = title
        self.year = year
        self.genre = genre
        self.times_played = times_played

    def __str__(self):
        return f"{self.title} ({self.year})"

    def __gt__(self, other):
        return self.title > other.title

    def play(self):
        self.times_played += 1

class Series(Movie):
    def __init__(self, title, year, genre, episode, season, times_played):
        super().__init__(title, year, genre, times_played)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"

    def __gt__(self, other):
        return self.title > other.title

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
rick_and_morty = Series("Rick and Morty", 2013, "Animation", 1, 1, 0)
pictures_list.append(rick_and_morty)
rocky = Movie("Rocky", 1976, "Drama", 0)
pictures_list.append(rocky)
shawshank_redemption = Movie("Shawshank Redemption", 1994, "Drama", 0)
pictures_list.append(shawshank_redemption)
elmo = Series("Elmo", 1979, "Comedy", 1, 1, 0)
pictures_list.append(elmo)

def get_movies(list):
    for item in list:
        movie_list = []
        if isinstance(item, Movie) and not isinstance(item, Series):
            movie_list.append(item)
        movie_list_sorted = sorted(movie_list, key=lambda movie: movie.title)
        for movie in movie_list_sorted:
            print(movie)

get_movies(pictures_list)

def get_series(list):
    for item in list:
        series_list = []
        if isinstance(item, Series):
            series_list.append(item)
        series_list_sorted = sorted(series_list, key=lambda series: series.title)
        for series in series_list_sorted:
            print(series)
get_series(pictures_list)

