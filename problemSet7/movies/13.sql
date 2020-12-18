SELECT DISTINCT P.name FROM (SELECT movies.id FROM ((stars INNER JOIN movies ON stars.movie_id = movies.id) INNER JOIN people ON stars.person_id = people.id) WHERE people.name = 'Kevin Bacon' AND people.birth = 1958) KB, (SELECT * FROM (stars INNER JOIN people ON stars.person_id = people.id)) P WHERE KB.id = P.movie_id AND P.name != 'Kevin Bacon';