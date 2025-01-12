CREATE DATABASE CompanyXYZ;
USE CompanyXYZ;
CREATE TABLE EmployeeInfo (
	id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT NOT NULL
    );
INSERT INTO EmployeeInfo
(id,name,salary)
VALUES
(1,"adam",25000),
(2,"bob",30000),
(3,"casey",45000);
SELECT * FROM EmployeeInfo;