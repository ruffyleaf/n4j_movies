# n4j_movies
Working on python bolt driver to familiarise with Neo4J.

## Setting up the environment
1. Create the conda environment
2. conda env create -f environment.yml
3. conda activate neo4j_test
4. pip install -r requirements.txt
5. n4j_movies is not on PyPI so one more pip install . to install n4j_movies in site-packages
6. Test that it works - run a python prompt and try `import n4j_movies`

## neo4j installation and setup
1. Download the neo4j server (desktop should work fine too) - https://neo4j.com/download-center/#releases
2. Save it some place.
3. Launch the server:
    D:\>neo4j\bin\neo4j console
    2018-11-01 02:33:05.982+0000 INFO  ======== Neo4j 3.4.9 ========
    2018-11-01 02:33:06.018+0000 INFO  Starting...
    2018-11-01 02:33:09.245+0000 INFO  Bolt enabled on 127.0.0.1:7687.
    2018-11-01 02:33:10.741+0000 INFO  Started.
    2018-11-01 02:33:11.434+0000 INFO  Remote interface available at http://localhost:7474/
4. Launch the browser - http://localhost:7474/
5. Populate the database with the movie data by starting - :play movies - in the browser prompt.

## Run main.py
1. python main.py
