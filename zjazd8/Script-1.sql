CREATE DATABASE homework5;

CREATE TABLE Uzytkownik (
	Id INT NOT NULL AUTO_INCREMENT,
	Imie VARCHAR(50) NOT NULL,
	Nazwisko VARCHAR(50) NOT NULL,
	PRIMARY KEY(Id)
	)

CREATE TABLE Zamowienie (
	Id INT NOT NULL AUTO_INCREMENT,
	Numer_zamowienia varchar(10) NOT NULL,
	PRIMARY KEY (Id)
	)

CREATE TABLE Produkt (
	Id INT NOT NULL AUTO_INCREMENT,
	Nazwa_produktu varchar(10) NOT NULL,
	PRIMARY KEY (Id)
	)
	
ALTER TABLE Zamowienie ADD Id_klienta int

ALTER TABLE Zamowienie ADD FOREIGN KEY (Id_klienta) REFERENCES Uzytkownik(Id)

ALTER TABLE Zamowienie ADD Id_produktu int

ALTER TABLE Zamowienie ADD FOREIGN KEY (Id_produktu) REFERENCES Produkt(Id)

INSERT INTO Uzytkownik VALUES (1, 'Jan', 'Paw')

INSERT INTO Uzytkownik VALUES (2, 'Michael', 'Jordan')

INSERT INTO Produkt VALUES (1, 'Rower')

INSERT INTO Produkt VALUES (2, 'Komputer')

INSERT INTO Zamowienie VALUES (1, 'AAA1', 1, 2)

INSERT INTO Zamowienie VALUES (2, 'AAA2', 2, 2)

INSERT INTO Zamowienie VALUES (3, 'AAA3', 2, 1)

SELECT * FROM Zamowienie
	
