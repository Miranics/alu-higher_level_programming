-- Script to create MySQL user user_0d_1 with all privileges and set password

-- Drop the user if it exists
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create the user
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes
FLUSH PRIVILEGES;

