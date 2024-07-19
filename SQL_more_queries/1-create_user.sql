-- Script to create MySQL user user_0d_1 with all privileges and set password

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';

-- Apply the changes
FLUSH PRIVILEGES;

