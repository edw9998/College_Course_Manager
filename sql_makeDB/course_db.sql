SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO"; -- This is preferred for MySQL.
SET SQL_SAFE_UPDATES = 0;               -- Suppress DML Query Warnings.
SET FOREIGN_KEY_CHECKS = 1;             -- Enable foreign key checking.
SET AUTOCOMMIT = 0;                     -- Disable autocommit.
SET time_zone = "+00:00";               -- Set time zone to UTC.

-- Create separate session.
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

-- Creates savepoint at current state of each table.
SAVEPOINT AT_CURRENT_STATE;

-- Verify savepoint and commit the final state.
ROLLBACK TO SAVEPOINT AT_CURRENT_STATE;
RELEASE SAVEPOINT AT_CURRENT_STATE;
COMMIT;
