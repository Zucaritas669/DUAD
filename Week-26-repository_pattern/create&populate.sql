DROP TABLE IF EXISTS lyfter_car_rental.rentals;
DROP TABLE IF EXISTS lyfter_car_rental.users;
DROP TABLE IF EXISTS lyfter_car_rental.cars;


SET search_path TO lyfter_car_rental;

CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL,
	username VARCHAR(40) NOT NULL,
	email VARCHAR(40) NOT NULL,
	password VARCHAR(40) NOT NULL,
	birth_date DATE NOT NULL,
	account_status VARCHAR(20) DEFAULT 'active' NOT NULL
	);


CREATE TABLE cars(
	id SERIAL PRIMARY KEY,
	brand VARCHAR(20) NOT NULL,
	model VARCHAR(20) NOT NULL,
	manufacture_year int NOT NULL,
	status VARCHAR(40) DEFAULT 'available'  NOT NULL
	);


CREATE TABLE rentals(
	id SERIAL PRIMARY KEY,
	user_id INT NOT NULL,
	car_id INT NOT NULL,
	rental_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	rental_status VARCHAR(40) DEFAULT 'active' NOT NULL,

	FOREIGN KEY(user_id) REFERENCES users(id),
	FOREIGN KEY(car_id) REFERENCES cars(id)
);


-- users
SET search_path TO lyfter_car_rental;

insert into users (name, username, email, password, birth_date) values ('Ulric', 'uclerke0', 'uondrusek0@buzzfeed.com', 'bV6%nPfFS>IJ@f,z', '2026-04-20');
insert into users (name, username, email, password, birth_date) values ('Geneva', 'gjefford1', 'galejandre1@omniture.com', 'mP7<u"3pmPW}<m', '2025-10-24');
insert into users (name, username, email, password, birth_date) values ('Roslyn', 'rwondraschek2', 'rwilton2@bandcamp.com', 'vI7|jKGUc!{HPF,W', '2026-01-17');
insert into users (name, username, email, password, birth_date) values ('Caryn', 'cwaleran3', 'cgilbride3@ovh.net', 'hO5="3X9kj_', '2026-03-07');
insert into users (name, username, email, password, birth_date) values ('Marena', 'mwrates4', 'mgabby4@purevolume.com', 'oY1&zX4nQ@CDh&', '2025-08-19');
insert into users (name, username, email, password, birth_date) values ('Lira', 'lcollelton5', 'lmeadmore5@google.de', 'wL8\cf0&}E/', '2025-07-20');
insert into users (name, username, email, password, birth_date) values ('Claus', 'cdooland6', 'caidler6@eventbrite.com', 'oP7)SE2F', '2025-10-04');
insert into users (name, username, email, password, birth_date) values ('Bamby', 'brydzynski7', 'bworham7@mapy.cz', 'dZ3.QsRW', '2025-07-16');
insert into users (name, username, email, password, birth_date) values ('Quintin', 'qygou8', 'qmurdoch8@scribd.com', 'qQ0_+UWz9ALi', '2026-02-28');
insert into users (name, username, email, password, birth_date) values ('Charita', 'cdargavel9', 'crosewall9@wsj.com', 'mD2?8.u%sCIiTn', '2026-01-31');
insert into users (name, username, email, password, birth_date) values ('Josie', 'jhalmkina', 'jblindta@google.co.uk', 'vT2}dwYx', '2025-10-08');
insert into users (name, username, email, password, birth_date) values ('Shaina', 'skhilkovb', 'scalderab@instagram.com', 'dV6,GnEeN', '2025-11-21');
insert into users (name, username, email, password, birth_date) values ('Katy', 'kfranciskiewiczc', 'kbinerc@dropbox.com', 'oZ1#JfxJovY(Oe9', '2025-07-19');
insert into users (name, username, email, password, birth_date) values ('Darsie', 'dterlindend', 'dmurtd@skyrock.com', 'oE9$ZS6f3iCo', '2025-10-27');
insert into users (name, username, email, password, birth_date) values ('Anny', 'afosdykee', 'avanhaulte@nba.com', 'vQ1?%W3rDz', '2025-11-29');
insert into users (name, username, email, password, birth_date) values ('Jacquelyn', 'jburchfieldf', 'jharlickf@google.nl', 'xI4,lT@g/TWKmj3&', '2025-08-14');
insert into users (name, username, email, password, birth_date) values ('Merrill', 'mskullyg', 'mwakeg@opensource.org', 'gM3|uyfTU', '2025-10-11');
insert into users (name, username, email, password, birth_date) values ('Delcina', 'dgilmartinh', 'dclineh@friendfeed.com', 'xW1%&${8`', '2026-04-25');
insert into users (name, username, email, password, birth_date) values ('Trevor', 'tlaveracki', 'tmccordi@uol.com.br', 'oO0"/!p6&R', '2026-03-28');
insert into users (name, username, email, password, birth_date) values ('Karlotte', 'kgrimblebyj', 'kjowlingj@opera.com', 'hW7$e*OLa1', '2025-11-03');
insert into users (name, username, email, password, birth_date) values ('Hildegarde', 'hfeldkleink', 'hhoughtk@yale.edu', 'pP2$iy~ZtvjHfc}W', '2026-05-21');
insert into users (name, username, email, password, birth_date) values ('Aldin', 'abletcherl', 'agrabehaml@github.com', 'qK1=0xffz', '2026-05-11');
insert into users (name, username, email, password, birth_date) values ('Belva', 'bcoitm', 'bbevirm@usatoday.com', 'uJ6{aSuyps', '2026-04-24');
insert into users (name, username, email, password, birth_date) values ('Kanya', 'kchatainn', 'kmerrigann@unesco.org', 'wX5&rO!\+#G,i$}', '2026-05-16');
insert into users (name, username, email, password, birth_date) values ('Brade', 'bkollacho', 'bcaddingo@zdnet.com', 'tR2(ed=.', '2026-03-19');
insert into users (name, username, email, password, birth_date) values ('Jenni', 'jmcgrannp', 'jdrancep@washingtonpost.com', 'sT6_KQ"X>ky|U', '2025-11-20');
insert into users (name, username, email, password, birth_date) values ('Brittney', 'bbayleq', 'byourellq@pen.io', 'sG4!m7{!', '2026-02-16');
insert into users (name, username, email, password, birth_date) values ('Fifi', 'fbarkshirer', 'fjobbr@github.io', 'iD3"=5b~Z@.{y=*!', '2025-10-26');
insert into users (name, username, email, password, birth_date) values ('Kris', 'ksokills', 'kgasquoines@deviantart.com', 'lS8$j(X/yp8_+N2o', '2026-04-28');
insert into users (name, username, email, password, birth_date) values ('Nikki', 'nmerseyt', 'nkimmelt@weebly.com', 'lK6\#k#>>LMiu6.', '2025-07-06');
insert into users (name, username, email, password, birth_date) values ('Cherida', 'chutchasonu', 'cmourtonu@ucoz.ru', 'kH4''BY8>1twgkw', '2025-06-28');
insert into users (name, username, email, password, birth_date) values ('Nataline', 'nkenderdinev', 'nmeiningerv@ask.com', 'vV4\WTER', '2025-09-15');
insert into users (name, username, email, password, birth_date) values ('Scot', 'srockliffew', 'sbeckersw@newsvine.com', 'tH3~\*4*&RVx$F', '2025-09-05');
insert into users (name, username, email, password, birth_date) values ('Ebenezer', 'ebyartx', 'ecopasx@ocn.ne.jp', 'lN3"B($IHS', '2026-02-07');
insert into users (name, username, email, password, birth_date) values ('Livvyy', 'lflindally', 'lstedey@nasa.gov', 'iI3@V\`2gIMvj', '2025-07-09');
insert into users (name, username, email, password, birth_date) values ('Travers', 'tbraunleinz', 'tkeelz@simplemachines.org', 'zM4=Q#j6"mq', '2026-03-19');
insert into users (name, username, email, password, birth_date) values ('Mamie', 'mjeenes10', 'mstanistrete10@tinyurl.com', 'zL4|?5TX~Kp', '2026-04-08');
insert into users (name, username, email, password, birth_date) values ('Emyle', 'ecollinwood11', 'ebravey11@arizona.edu', 'jA1*8&mO"U>L~6', '2026-06-16');
insert into users (name, username, email, password, birth_date) values ('Clemence', 'cfairchild12', 'cfishly12@icq.com', 'aD9%${tr', '2026-05-25');
insert into users (name, username, email, password, birth_date) values ('Aliza', 'aizen13', 'afulmen13@taobao.com', 'wL3.*7U04RA"dH', '2026-04-12');
insert into users (name, username, email, password, birth_date) values ('Zachery', 'zpaff14', 'zfernant14@oakley.com', 'nH7*U@02pf', '2025-09-12');
insert into users (name, username, email, password, birth_date) values ('Harris', 'hsloan15', 'hsaundercock15@ycombinator.com', 'tM1(vwFbFf1I', '2026-01-05');
insert into users (name, username, email, password, birth_date) values ('Niki', 'nnuth16', 'nrulten16@omniture.com', 'qD8#.Bib=n&', '2025-11-22');
insert into users (name, username, email, password, birth_date) values ('Culley', 'clippiett17', 'ctinker17@constantcontact.com', 'wA9$VNX~Zm88jH2', '2025-08-15');
insert into users (name, username, email, password, birth_date) values ('Rubi', 'rmaly18', 'rnorthbridge18@uol.com.br', 'vV8(JTlw&', '2025-08-23');
insert into users (name, username, email, password, birth_date) values ('Devonne', 'ddoy19', 'damort19@independent.co.uk', 'kJ7~et$w4&n', '2025-09-07');
insert into users (name, username, email, password, birth_date) values ('Kendell', 'kcremins1a', 'kneilson1a@tinyurl.com', 'kU3!ZnB2', '2025-08-04');
insert into users (name, username, email, password, birth_date) values ('Onida', 'opink1b', 'obalogh1b@google.co.jp', 'uQ9~d.wHX@M\qy&B', '2025-10-03');
insert into users (name, username, email, password, birth_date) values ('Manolo', 'mmesnard1c', 'mlearmond1c@timesonline.co.uk', 'iO3.jySysk@{f)L', '2026-02-19');
insert into users (name, username, email, password, birth_date) values ('Ardra', 'aschorah1d', 'anason1d@altervista.org', 'vD2,0?cxtAqH', '2026-04-28');

---------------------------------------------------------------------------------------------------------------------------------------------------------


-- cars
insert into cars (brand, model, manufacture_year) values ('Buick', 'Park Avenue', 1996);
insert into cars (brand, model, manufacture_year) values ('Mercury', 'Sable', 1995);
insert into cars (brand, model, manufacture_year) values ('Nissan', 'Quest', 2012);
insert into cars (brand, model, manufacture_year) values ('Cadillac', 'Escalade', 2004);
insert into cars (brand, model, manufacture_year) values ('Jeep', 'Compass', 2009);
insert into cars (brand, model, manufacture_year) values ('BMW', 'M6', 2009);
insert into cars (brand, model, manufacture_year) values ('Fillmore', 'Fillmore', 1960);
insert into cars (brand, model, manufacture_year) values ('Chevrolet', 'S10', 1995);
insert into cars (brand, model, manufacture_year) values ('Saab', '9000', 1997);
insert into cars (brand, model, manufacture_year) values ('Volkswagen', 'Tiguan', 2012);
insert into cars (brand, model, manufacture_year) values ('Chevrolet', 'Express 3500', 2009);
insert into cars (brand, model, manufacture_year) values ('Honda', 'Civic', 2005);
insert into cars (brand, model, manufacture_year) values ('Dodge', 'Ram 2500 Club', 1997);
insert into cars (brand, model, manufacture_year) values ('Land Rover', 'Defender Ice Edition', 2010);
insert into cars (brand, model, manufacture_year) values ('Ford', 'E-Series', 1992);
insert into cars (brand, model, manufacture_year) values ('Chevrolet', 'S10 Blazer', 1994);
insert into cars (brand, model, manufacture_year) values ('GMC', 'Savana Cargo Van', 2006);
insert into cars (brand, model, manufacture_year) values ('Ford', 'Econoline E150', 1993);
insert into cars (brand, model, manufacture_year) values ('Volvo', 'S60', 2012);
insert into cars (brand, model, manufacture_year) values ('Saab', '9-3', 2002);
insert into cars (brand, model, manufacture_year) values ('Volkswagen', 'rio', 2002);
insert into cars (brand, model, manufacture_year) values ('Mercury', 'Capri', 1992);
insert into cars (brand, model, manufacture_year) values ('Cadillac', 'DTS', 2007);
insert into cars (brand, model, manufacture_year) values ('Volkswagen', 'Type 2', 1988);
insert into cars (brand, model, manufacture_year) values ('Kia', 'Sedona', 2012);
insert into cars (brand, model, manufacture_year) values ('Toyota', 'Avalon', 2002);
insert into cars (brand, model, manufacture_year) values ('GMC', 'Rally Wagon 2500', 1994);
insert into cars (brand, model, manufacture_year) values ('Plymouth', 'Sundance', 1994);
insert into cars (brand, model, manufacture_year) values ('Dodge', 'Avenger', 2011);
insert into cars (brand, model, manufacture_year) values ('BMW', '745', 2004);
insert into cars (brand, model, manufacture_year) values ('Chrysler', 'PT Cruiser', 2003);
insert into cars (brand, model, manufacture_year) values ('Lincoln', 'MKX', 2007);
insert into cars (brand, model, manufacture_year) values ('Dodge', 'Ram 2500', 2000);
insert into cars (brand, model, manufacture_year) values ('Mazda', 'RX-7', 1992);
insert into cars (brand, model, manufacture_year) values ('Jaguar', 'XF', 2010);
insert into cars (brand, model, manufacture_year) values ('Ford', 'Transit Connect', 2013);
insert into cars (brand, model, manufacture_year) values ('Chrysler', 'Cirrus', 1997);
insert into cars (brand, model, manufacture_year) values ('Saab', '9-3', 2001);
insert into cars (brand, model, manufacture_year) values ('GMC', 'Yukon XL 2500', 2003);
insert into cars (brand, model, manufacture_year) values ('BMW', '7 Series', 2010);
insert into cars (brand, model, manufacture_year) values ('BMW', '7 Series', 2005);
insert into cars (brand, model, manufacture_year) values ('Mercury', 'Cougar', 1994);
insert into cars (brand, model, manufacture_year) values ('Lincoln', 'Town Car', 2006);
insert into cars (brand, model, manufacture_year) values ('Chevrolet', 'S10', 1999);
insert into cars (brand, model, manufacture_year) values ('Chrysler', '300M', 2001);
insert into cars (brand, model, manufacture_year) values ('Acura', 'RL', 1998);
insert into cars (brand, model, manufacture_year) values ('Honda', 'CR-V', 2010);
insert into cars (brand, model, manufacture_year) values ('Mazda', 'B-Series', 1996);
insert into cars (brand, model, manufacture_year) values ('Chevrolet', 'Express 2500', 2010);
insert into cars (brand, model, manufacture_year) values ('Jeep', 'Wrangler', 1998);
----------------------------------------------------------------------------------------------

Tarea 2: Pruebas básicas de la DB
Con la DB creada, cree los siguientes scripts:

Un script que agregue un usuario nuevo
INSERT INTO users(name, username , email, password , birth_date) VALUES
('Shalston', 'shalston97', 'shalston97@gmail.com','pass123', '2003-08-27')


Un script que agregue un automovil nuevo
INSERT INTO cars(brand, model, manufacture_year) VALUES
('Nissan', 'Silvia', '1996')


Un script que cambie el estado de un usuario
UPDATE users
SET account_status = 'disabled'
WHERE id = 1;


Un script que cambie el estado de un automovil
UPDATE cars
SET status = 'disabled'
WHERE id = 5;


Un script que genere un alquiler nuevo con los datos de un usuario y un automovil
INSERT INTO rentals (user_id , car_id)
VALUES (1,5);

-- Nota
-- Solo se ingresan estos, porque los demás se generan automaticamente


Un script que confirme la devolución del auto al completar el alquiler, colocando el auto como disponible y completando el estado del alquiler
UPDATE cars
SET status = 'available'
WHERE id = 5;

UPDATE rentals
SET rental_status = 'completed'
WHERE id = 1;


Un script que deshabilite un automovil del alquiler
UPDATE cars
SET status = 'disabled'
WHERE id = 5;


Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles.
SELECT * FROM cars
WHERE status = 'available';

SELECT * FROM cars
WHERE status = 'rented';
