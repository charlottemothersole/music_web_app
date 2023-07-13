DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  artist text
);