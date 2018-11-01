from neo4j.v1 import GraphDatabase

class Actor(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)

    def close(self):
        self._driver.close()

    def create_actor(self, name):
        with self._driver.session() as session:
            session.write_transaction(self.create_actor_node, name)

    @staticmethod
    def create_actor_node(tx, name):
        tx.run(
            "MERGE (a:Person {name: $name})", name=name
        )                

    def get_actor(self, name):
        with self._driver.session() as session:
            tx = session.begin_transaction()
            result = self.retrieve_actor(tx, name)

        return result["name"]
    
    @staticmethod
    def retrieve_actor(tx, actor_name):
        return tx.run(
            "MATCH (actor {name: $name})"
            "RETURN actor", name=actor_name
        ).single().value()

    def get_actors(self):
        with self._driver.session() as session:
            tx = session.begin_transaction()
            result = self.retrieve_actors(tx)
            
        return result
    
    @staticmethod
    def retrieve_actors(tx):
        return tx.run(
            "MATCH (p:Person) - [:ACTED_IN] - ()"
            "RETURN DISTINCT p.name"            
        ).value()
    
    def get_actor_count(self):
        with self._driver.session() as session:
            tx = session.begin_transaction()
            count = tx.run(
                        "MATCH (people:Person)" 
                        "RETURN count(people)")
        return count.value()
    
    def get_actors_in_movie(self, movie):
        with self._driver.session() as session:
            tx = session.begin_transaction()
            result = self.retrieve_actors_in_movie(tx, movie)
            
        return result
    
    @staticmethod
    def retrieve_actors_in_movie(tx, movie):
        return tx.run(
                "MATCH (actors)-[:ACTED_IN]->(:Movie {title: $movie})"
                "RETURN actors.name", 
            movie=movie).value()