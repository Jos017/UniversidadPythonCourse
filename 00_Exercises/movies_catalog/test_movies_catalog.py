from domain.Movie import Movie
from service.Movies_catalog import Movies_catalog

option = None
while option != 4:
    try:
        print('\n', 'Options'.center(50, '-'))
        print('1. Add Movie')
        print('2. List Movies')
        print('3. Delete Movies Catalog')
        print('4. Exit')
        option = int(input('Select your option (1 - 4): '))
        match option:
            case 1:
                movie_name = input('What is the movie name?: ')
                movie = Movie(movie_name)
                Movies_catalog.add_movie(movie)
            case 2:
                Movies_catalog.list_movies()
            case 3:
                Movies_catalog.delete_movies()
            case 4:
                pass
            case _:
                raise ValueError('Not in range 1 - 4')
    except ValueError as e:
        print(f'An error has ocurred: {e}')
        option = None

print('Exit program...')
