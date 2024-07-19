-- Script to list all privileges of MySQL users user_0d_1 and user_0d_2 on the server

-- Check if user_0d_1 exists and show their grants if they do
SELECT 
    IF(
        EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost'), 
        'SHOW GRANTS FOR ''user_0d_1''@''localhost'';', 
        'SELECT ''User user_0d_1 does not exist'''
    ) AS statement 
INTO @statement_1;
PREPARE stmt_1 FROM @statement_1;
EXECUTE stmt_1;
DEALLOCATE PREPARE stmt_1;

-- Check if user_0d_2 exists and show their grants if they do
SELECT 
    IF(
        EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost'), 
        'SHOW GRANTS FOR ''user_0d_2''@''localhost'';', 
        'SELECT ''User user_0d_2 does not exist'''
    ) AS statement 
INTO @statement_2;
PREPARE stmt_2 FROM @statement_2;
EXECUTE stmt_2;
DEALLOCATE PREPARE stmt_2;

