-- Cities by States

SELECT id, name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;
