-- Script that all lists all cities of California that can be found in databases hbt_0d_usa.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
