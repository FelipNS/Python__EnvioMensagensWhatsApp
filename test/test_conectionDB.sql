USE Classes;

CREATE TABLE classesName (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30) NOT NULL
);

TRUNCATE TABLE classesName;
SELECT * FROM classesName;
INSERT INTO classesName(name) VALUES ('1°ANO PONTE NOVA');
INSERT INTO classesName(name) VALUES ('Mãe Linda♥');
INSERT INTO classesName(name) VALUES ('1°e 2° PERÍODO PONTE NOVA');
RENAME TABLE classes TO classesName;
