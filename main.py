from n4j_movies.models.actor import Actor
from n4j_movies.models.movie import Movie

def main():
    URI = 'bolt://localhost:7687'
    USER = 'neo4j'
    PASSWORD = '1qaz2wsx'

    actor = Actor(URI, USER, PASSWORD)

    print actor.get_actor("Tom Hanks")
    print actor.get_actor_count()
    for a in actor.get_actors_in_movie("The Matrix"):
        print a

    movie = Movie(URI, USER, PASSWORD)

    for m in movie.get_movies():
        print "The Actors in %s are:" % m
        for a in actor.get_actors_in_movie(m):
            print a
        
        print "-----"

if __name__ == '__main__':
    main()