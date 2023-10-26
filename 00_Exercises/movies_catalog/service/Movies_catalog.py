import os


class Movies_catalog:
    # Get the script directory
    __script_directory = os.path.dirname(os.path.abspath(__file__))
    # Get the parent directory
    __parent_directory = os.path.dirname(__script_directory)

    file_route = os.path.join(__parent_directory, 'movies.txt')

    @classmethod
    def add_movie(cls, movie):
        with open(cls.file_route, 'a', encoding='utf8') as file:
            file.write(f'{movie.name}\n')

    @classmethod
    def list_movies(cls):
        with open(cls.file_route, 'r', encoding='utf8') as file:
            print('Movies catalog'.center(50, '-'))
            print(file.read())

    @classmethod
    def delete_movies(cls):
        os.remove(cls.file_route)
        print(f'File deleted: {cls.file_route}')
