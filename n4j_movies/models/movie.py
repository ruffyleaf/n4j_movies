from neo4j.v1 import GraphDatabase

class Movie(object):
    
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)
        
    def close(self):
        self._driver.close()
    
    def get_movies(self):
        with self._driver.session() as session:
            tx = session.begin_transaction()
            result = self.retrieve_movies(tx)
            
        return result
            
    @staticmethod
    def retrieve_movies(tx):
        return tx.run(
            "MATCH () - [] - (m:Movie)"
            "RETURN DISTINCT m.title"
        ).value()
    
    def get_movie_count(self):
        with self._driver.session() as session:
            tx = session.begin_transaction()
            result = self.count_movies(tx)
            
        return result
    
    @staticmethod
    def count_movies(tx):
        return tx.run(
            "MATCH (m:Movie)"
            "RETURN count(m)"
        ).value()
    
    def get_movies_of_actor(self, actor_name):
        with self._driver.session() as session:
            tx = session.begin_transaction()
            result = self.retrieve_actors_movies(tx, actor_name)
            
        return result
    
    @staticmethod
    def retrieve_actors_movies(tx, name):
        return tx.run(
            "MATCH (:Person {name: $name}) - [a:ACTED_IN] -> (movies)"
            "RETURN movies.title, a.roles", name=name).values()