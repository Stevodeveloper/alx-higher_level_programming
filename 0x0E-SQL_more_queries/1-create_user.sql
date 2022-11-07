-- creates the MySQL server user user_0d_1. 
-- The user_0d_1 password should be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, the scrip will not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH 'user_0d_1_pwd';
GRANT ALL PRIVILEGDES ON * . * TO 'user_0d_1'@'localhost';
FLUSH PRIVILEDGES; 
