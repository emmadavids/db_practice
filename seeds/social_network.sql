DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name text,
  email text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user_id foreign key(user_id)
    references users(id)
    on delete cascade
);


INSERT INTO users (name, email) VALUES ('John Doe', 'johndoe@example.com');
INSERT INTO users (name, email) VALUES ('Jane Smith', 'janesmith@example.com');

-- Inserting data into the posts table
INSERT INTO posts (title, content, views, user_id) VALUES ('My First Post', 'This is my first post.', 10, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Second Post', 'This is my second post.', 5, 2);