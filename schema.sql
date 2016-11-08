--drop table if exists users;
-- drop table if exists trips;

-- -- create table users (
-- -- 	username text not null primary key,
-- -- 	password text not null
-- -- );

-- create table trips (
-- 	-- trip_number integer not null,
-- 	trip_name text not null,
-- 	destination text not null,
-- 	username text not null,
-- 	friend text not null,
-- 	foreign key(username) references users(username),
-- 	primary key(trip_name, username)
-- );
