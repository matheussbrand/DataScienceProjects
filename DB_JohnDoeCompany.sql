-- Tiktok Clone Generic Datbase for John Doe Company

-- Users table store information about registered users
CREATE TABLE users(
    id INT PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL, -- Unique Username
    email VARCHAR(100) NOT NULL, -- Unique Email
    password VARCHAR(100) NOT NULL,
    profile_pic VARCHAR(255), -- Profile Picture Location
    joined_date DATE NOT NULL -- Date user signed up
);


-- Videos table to store user uploaded videos
CREATE TABLE videos(
    id INT PRIMARY KEY AUTOINCREMENT,
    user_id INT NOT NULL, -- Foreign key to users table
    videos_url VARCHAR(255) NOT NULL, -- Location of videos file
    description TEXT, -- Description entered by user
    likes INT DEFAULT 0, -- Number of shares
    shares INT DEFAULT 0, -- Number of comments
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date video was uploaded
);


-- Language table to store supported languages
CREATE TABLE language( id INT PRIMARY KEY,
    id_language VARCHAR(10) NOT NULL UNIQUE, -- eg. PT-BR, JP, EN, FR
    language_name VARCHAR(100) NOT NULL
);

-- Hastags table to track hashtagged videos
CREATE TABLE hashtags(
    id INT PRIMARY KEY AUTOINCREMENT,
    hashtag VARCHAR(100) NOT NULL UNIQUE,
    videos INT DEFAULT 0 -- Count of videos with this hashtag
);


-- Hashtag mapping table
CREATE TABLE videos_hashtags(
    id INT PRIMARY KEY AUTOINCREMENT,
    videos_id INT NOT NULL,
    hashtag_id INT NOT NULL,
);


-- Music table to store available music tracks
CREATE TABLE music(
    id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    artist VARCHAR(100) NOT NULL,
    file_path VARCHAR(255) NOT NULL
);


-- Music mapping table
CREATE TABLE video_music(
    id INT PRIMARY KEY AUTOINCREMENT,
    video_id INT NOT NULL,
    music_id INT NOT NULL
);


-- Comments table to store comments on videos
CREATE TABLE comments(
    id INT PRIMARY KEY AUTOINCREMENT,
    user_id INT NOT NULL, -- Foreing key to users table
    video_id INT NOT NULL,  -- Foreing key to videos table
    comment TEXT NOT NULL, -- Actual text content of comment
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date comment was posted
);


-- Likes table to track what videos a user has liked
CREATE TABLE likes(
    id INT PRIMARY KEY AUTOINCREMENT,
    user_id INT NOT NULL,
    videos_id INT NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Location table to locate videos
CREATE TABLE localizations(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL
);


-- Videos-location mapping table
CREATE TABLE video_locations(
    id INT PRIMARY KEY AUTOINCREMENT,
    video_id INT NOT NULL,
    location_id INT NOT NULL
);


