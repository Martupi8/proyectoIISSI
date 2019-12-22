USE grados;

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Tutorials;
DROP TABLE IF EXISTS Appointments;
SET FOREIGN_KEY_CHECKS = 1;

-- Tabla de Profesores
CREATE TABLE Teachers(
	teacherId INT NOT NULL AUTO_INCREMENT,
	dni CHAR(9) NOT NULL UNIQUE,
	firstName VARCHAR(100) NOT NULL,
	surname VARCHAR(100) NOT NULL,
	birthDate DATE NOT NULL,
	email VARCHAR(250) NOT NULL UNIQUE,
	category VARCHAR(30) NOT NULL,
	PRIMARY KEY (teacherId),
	CONSTRAINT invalidTeacherCategory CHECK (category IN ('Catedrático', 'Titular de Universidad', 'Profesor Contratado Doctor', 'Profesor Ayudante Doctor'))
); 

-- Tabla de Alumnos
CREATE TABLE Students(
	studentId INT NOT NULL AUTO_INCREMENT,
	accessMethod VARCHAR(30) NOT NULL,
	dniSt CHAR(9) NOT NULL UNIQUE,
	firstNameSt VARCHAR(100) NOT NULL,
	surnameSt VARCHAR(100) NOT NULL,
	birthDateSt DATE NOT NULL,
	emailSt VARCHAR(250) NOT NULL UNIQUE,
	PRIMARY KEY (studentId),
	CONSTRAINT invalidStudentAccessMethod CHECK (accessMethod IN ('Selectividad', 'Ciclo', 'Mayor', 'Titulado Extranjero'))
);

-- Tabla de Tutorías
CREATE TABLE Tutorials(
	tutorialId INT NOT NULL AUTO_INCREMENT,
 	dayWeek VARCHAR(100) NOT NULL,
 	startTime TIME NOT NULL,
 	endTime TIME NOT NULL,
 	teacherId INT,
 	PRIMARY KEY (tutorialId),
 	FOREIGN KEY (teacherId) REFERENCES Teachers (teacherId) ON DELETE SET NULL,
 	CONSTRAINT invalidTutorialWeekday CHECK (dayWeek IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'))
);

-- Tabla de Citas
CREATE TABLE Appointments(
	appointmentId INT NOT NULL AUTO_INCREMENT,
	dateAppointment DATE NOT NULL,
	hourAppointment TIME NOT NULL,
	tutorialId INT NOT NULL,
	studentId INT NOT NULL,
	PRIMARY KEY (appointmentId),
	FOREIGN KEY (tutorialId) REFERENCES Tutorials (tutorialId) ON DELETE CASCADE,
	FOREIGN KEY (studentId) REFERENCES Students (studentId) ON DELETE CASCADE,
	UNIQUE (dateAppointment, hourAppointment)
);

INSERT INTO Teachers(dni, firstName, surname, birthDate, email, category) VALUES
('34567890C', 'Juan Carlos', 'Roldán Salvador', '1970-08-16', 'jcroldan@us.es', 'Profesor Ayudante Doctor'),
('34557790K', 'Rafael', 'Corchuelo Gil', '1967-05-26', 'corchu@lsi.us.es', 'Titular de Universidad'),
('18475639M', 'Luis Miguel', 'Soria Morillo', '1977-05-13', 'lsoria@us.es', 'Profesor Ayudante Doctor'),
('93652074E', 'Vicente', 'Carrillo Montero', '1969-09-03', 'carrillo@lsi.us.es', 'Titular de Universidad'),
('57942864R', 'Luisa', 'Romero Moreno', '1979-11-18', 'mariaro@us.es', 'Titular de Universidad'),
('48637537L', 'Daniel', 'Mateos García', '1977-05-13', 'mateosg@us.es', 'Profesor Ayudante Doctor'),
('56787537J', 'José C.', 'Riquelme Santos', '1967-04-19', 'riquelme@lsi.us.es', 'Catedrático'),
('45678878T', 'Fernando', 'Enríquez de Salamanca Ros', '1967-04-19', 'fenros@us.es', 'Profesor Contratado Doctor'),
('45677548T', 'Isabel A.', 'Nepomuceno Chamorro', '1975-08-09', 'isabel@lsi.us.es', 'Profesor Ayudante Doctor'),
('43456858S', 'Fernando', 'Fernández Machuca', '1976-12-17', 'ferfern@us.es', 'Profesor Ayudante Doctor');

INSERT INTO Students (accessMethod, dniSt, firstnameSt, surnameSt, birthdateSt, emailSt) VALUES
	('Selectividad', '12345678A', 'Daniel', 'Pérez', '1991-01-01', 'daniel@alum.us.es'),
	('Selectividad', '22345678A', 'Rafael', 'Ramírez', '1992-01-01', 'rafael@alum.us.es'),
	('Selectividad', '32345678A', 'Gabriel', 'Hernández', '1993-01-01', 'gabriel@alum.us.es'),
	('Selectividad', '42345678A', 'Manuel', 'Fernández', '1994-01-01', 'manuel@alum.us.es'),
	('Selectividad', '52345678A', 'Joel', 'Gómez', '1995-01-01', 'joel@alum.us.es'),
	('Selectividad', '62345678A', 'Abel', 'López', '1996-01-01', 'abel@alum.us.es'),
	('Selectividad', '72345678A', 'Azael', 'González', '1997-01-01', 'azael@alum.us.es'),
	('Selectividad', '8345678A', 'Uriel', 'Martínez', '1998-01-01', 'uriel@alum.us.es'),
	('Selectividad', '92345678A', 'Gael', 'Sánchez', '1999-01-01', 'gael@alum.us.es'),
	('Titulado Extranjero', '12345678B', 'Noel', 'Álvarez', '1991-02-02', 'noel@alum.us.es'),
	('Titulado Extranjero', '22345678B', 'Ismael', 'Antúnez', '1992-02-02', 'ismael@alum.us.es'),
	('Titulado Extranjero', '32345678B', 'Nathanael', 'Antolinez', '1993-02-02', 'nathanael@alum.us.es'),
	('Titulado Extranjero', '42345678B', 'Ezequiel', 'Aznárez', '1994-02-02', 'ezequiel@alum.us.es'),
	('Titulado Extranjero', '52345678B', 'Ángel', 'Chávez', '1995-02-02', 'angel@alum.us.es'),
	('Titulado Extranjero', '62345678B', 'Matusael', 'Gutiérrez', '1996-02-02', 'matusael@alum.us.es'),
	('Titulado Extranjero', '72345678B', 'Samael', 'Gálvez', '1997-02-02', 'samael@alum.us.es'),
	('Titulado Extranjero', '82345678B', 'Baraquiel', 'Ibáñez', '1998-02-02', 'baraquiel@alum.us.es'),
	('Titulado Extranjero', '92345678B', 'Otoniel', 'Idiáquez', '1999-02-02', 'otoniel@alum.us.es'),
	('Titulado Extranjero', '12345678C', 'Niriel', 'Benítez', '1991-03-03', 'niriel@alum.us.es'),
	('Titulado Extranjero', '22345678C', 'Múriel', 'Bermúdez', '1992-03-03', 'muriel@alum.us.es'),
	('Titulado Extranjero', '32345678C', 'John', 'AII', '2000-01-01', 'john@alum.us.es');
	
INSERT INTO Tutorials(dayWeek, startTime, endTime, teacherId) VALUES ('Tuesday', '10:40:00', '12:30:00', 1), 
('Thursday', '12:40:00', '14:30:00', 1), ('Monday', '12:40:00', '14:30:00', 2), ('Wednesday', '10:40:00', '12:30:00', 2),
('Friday', '08:30:00', '10:20:00', 3), ('Monday', '12:40:00', '14:30:00', 3), ('Wednesday', '08:30:00', '10:20:00', 4),
('Thursday', '12:40:00', '14:30:00', 4), ('Tuesday', '12:40:00', '14:30:00', 5), ('Friday', '10:40:00', '12:30:00', 5);

INSERT INTO Appointments(dateAppointment, hourAppointment, tutorialId, studentId) VALUES ('2019-11-19', '11:30:00', 1, 2),
('2019-11-28', '12:50:00', 2, 3), ('2019-11-04', '13:30:00', 3, 4), ('2019-11-06', '11:30:00', 4, 5);