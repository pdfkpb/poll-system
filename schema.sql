DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS poll;
DROP TABLE IF EXISTS options;

CREATE TABLE users (
  username TEXT PRIMARY KEY,
  password TEXT NOT NULL,
  is_admin INTEGER
);

CREATE TABLE poll (
  poll_id INTEGER PRIMARY KEY,
  author TEXT NOT NULL,
  title TEXT NOT NULL,
  FOREIGN KEY (author) REFERENCES users(username)
);

CREATE TABLE options (
    option_id INTEGER PRIMARY KEY AUTOINCREMENT,
    poll_id INTEGER NOT NULL,
    option_text TEXT NOT NULL,
    option_image TEXT,
    tally INTEGER,
    FOREIGN KEY (poll_id) REFERENCES poll(poll_id)
);