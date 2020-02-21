-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS cedric;

CREATE TABLE cedric (
  id INT NOT NULL AUTO_INCREMENT,
  nom VARCHAR(45) NULL,
  prenom VARCHAR(45) NULL,
  age VARCHAR(45) NULL,
  PRIMARY KEY (id));
