-- converts hbtn_0c_0 database to UTF8
-- converts the database to a UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
-- switches the Database
USE hbtn_0c_0;
-- alters the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
