DROP TABLE IF EXISTS Post_Comment CASCADE;


CREATE TABLE [IF NOT EXISTS] user(
    id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	-- created_on TIMESTAMP NOT NULL,
    -- last_login TIMESTAMP
);

CREATE TABLE [IF NOT EXISTS] post(
    id SERIAL order by user_name desc,
    user_name VARCHAR(50) PRIMARY KEY,
    title VARCHAR(150),
    category VARCHAR(100),
    summary TEXT,
    content TEXT, 
    publish_time TIMESTAMP NOT NULL VALUES(now()),
    tag SERIAL 
);


CREATE TABLE Post_Comment(
    id SERIAL ,
    post_id BIGSERIAL ,
    Guest_name VARCHAR(100),
    publish_Time TIMESTAMP NOT NULL VALUES(now()),
    content TEXT

);