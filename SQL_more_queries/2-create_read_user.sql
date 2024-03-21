-- creating database of htbn_0d_2 with user user_0d_2
-- Database has privilege layers so users with permission get password user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS "user_0d_2"@"localhost" IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT ON `hbtn_0d_2`.* TO "user_0d_2"@"localhost";