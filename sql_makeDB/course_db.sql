SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";         -- This is preferred for MySQL.
SET SQL_SAFE_UPDATES = 0;                       -- Suppress DML Query Warnings.
SET FOREIGN_KEY_CHECKS = 1;                     -- Disable foreign key checking.
SET AUTOCOMMIT = 0;                             -- Disable autocommit.
SET time_zone = "+00:00";                       -- Set time zone to UTC.

-- Create a separate session.
START TRANSACTION;

-- DB : 'CourseDB'
CREATE DATABASE IF NOT EXISTS CourseDB DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE CourseDB;

-- First Table : 'Teachers'
CREATE TABLE Teachers (
    teacher_id INT NOT NULL, 
    first_name VARCHAR(50) DEFAULT 'NONE', 
    last_name VARCHAR(50) DEFAULT 'NONE', 
    language_utilized VARCHAR(25), 
    teachingSince YEAR, 
    tax_id CHAR(10) UNIQUE, 
    phone_number VARCHAR(20) UNIQUE, 
    PRIMARY KEY (teacher_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Second Table : 'Courses'
CREATE TABLE Courses (
    course_id INT NOT NULL, 
    course_name VARCHAR(255) NOT NULL, 
    final_score FLOAT NOT NULL, 
    level ENUM('Beginner','Intermediate','Expert') NOT NULL, 
    course_price_usd FLOAT NOT NULL, 
    start_date DATE, 
    teacher_id INT, 
    PRIMARY KEY (course_id), 
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Third Table : 'Clients'
CREATE TABLE Clients (
    client_id INT NOT NULL, 
    client_name VARCHAR(40) NOT NULL, 
    address VARCHAR(100) DEFAULT 'NONE', 
    industry VARCHAR(50) NOT NULL, 
    PRIMARY KEY (client_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Fourth Table : 'Participants'
CREATE TABLE Participants (
    participant_id INT NOT NULL, 
    first_name VARCHAR(40) NOT NULL, 
    last_name VARCHAR(40) NOT NULL, 
    phone_no VARCHAR(20) UNIQUE NOT NULL, 
    client_designated INT, 
    PRIMARY KEY (participant_id), 
    FOREIGN KEY (client_designated) REFERENCES Clients(client_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Fifth Table : 'Course_History'
CREATE TABLE Course_History (
    participant_id INT, 
    course_id INT, 
    PRIMARY KEY (participant_id), 
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id), 
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- Inserts testing data.
INSERT INTO Teachers(teacher_id, first_name, last_name, language_utilized, teachingSince, tax_id, phone_number) VALUES 
(1791, 'Mona', 'Megistus', 'English', '1999', 'T-0195710', '(+1)9104810294'),
(8954, 'Diluc', 'Ragnvindr', 'English', '2012', 'T-8560924', '(+1)0194123124'),
(9542, 'Kaeya', 'Alberich', 'English', '2001', 'T-1940241', '(+1)9014291022'),
(2001, 'Sangonomiya', 'Kokomi', 'Japanese', '2015', 'T-1923014', '(+1)8102943019'),
(8465, 'Kamisato', 'Ayaka', 'Japanese', '2007', 'T-1849291', '(+1)9182477212');

INSERT INTO Courses(course_id, course_name, final_score, level, course_price_usd, start_date, teacher_id) VALUES
(90999, 'Fundamentals Of Astrology', 85.55, 'Expert', 89.99, '2007-01-14', 1791),
(81099, 'Fire Science V', 76.88, 'Expert', 74.99, '2015-08-09', 8954),
(75662, 'Glaciology I', 99.80, 'Beginner', 25.99, '2020-12-02', 9542),
(32165, 'Ancient Medical Practices', 87.76, 'Intermediate', 45.99, '2021-06-11', 2001),
(74111, 'Live C++ Course : From The Basics', 73.42, 'Intermediate', 35.99, '2008-09-19', 8465);

INSERT INTO Clients(client_id, client_name, address, industry) VALUES
(78342666, 'Razor', 'Wolvendom, Mondstadt', 'Dawn Winery'),
(98101822, 'Zhongli', 'Qixing, Liyue', 'The Shrine Of Depths'),
(87673211, 'Kaedahara Kazuha', 'Narukami Island, Inazuma', 'The Tenshukaku'),
(65768900, 'Sister Rosaria', 'Starfell Valley, Mondstadt', 'Dawn Winery'),
(43678921, 'Lady Ningguang', 'Liyue Harbor, Liyue', 'The Northland Bank');

INSERT INTO Participants(participant_id, first_name, last_name, phone_no, client_designated) VALUES
(751, 'Hu', 'Tao', '(+1)1902349188', 78342666),
(750, 'Xing', 'Qiu', '(+1)1615234909', 98101822),
(621, 'Eula', 'Lawrence', '(+1)8432327909', 87673211),
(422, 'Bei', 'Dou', '(+1)1115674831', 65768900),
(991, 'Yan', 'Fei', '(+1)2546743277', 43678921);

INSERT INTO Course_History(participant_id, course_id) VALUES
(751, 90999),
(750, 81099),
(621, 75662),
(422, 32165),
(991, 74111);

-- Creates savepoint at current state of each table.
SAVEPOINT AT_CURRENT_STATE;

-- Verify savepoint and commit final state.
ROLLBACK TO SAVEPOINT AT_CURRENT_STATE;
RELEASE SAVEPOINT AT_CURRENT_STATE;
COMMIT;