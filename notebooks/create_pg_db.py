import psycopg2

conn = psycopg2.connect(
    host="postgres",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432",
)

cur = conn.cursor()

# -- Drop the 'messages' table if it exists
cur.execute("DROP TABLE IF EXISTS messages;")
conn.commit()

# -- Create the 'messages' table
# cur.execute(
#     """CREATE TABLE messages (
#     id SERIAL PRIMARY KEY,
#     time TIMESTAMP,
#     message_id VARCHAR(255),
#     client_id INTEGER,
#     amount INTEGER);"""
# )


cur.execute(
    """
    CREATE TABLE messages (
        id SERIAL PRIMARY KEY,
        time TIMESTAMP,
        message_id VARCHAR(255),
        client_id INTEGER,
        amount INTEGER,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        gender VARCHAR(50),
        country_id INTEGER,
        country VARCHAR(255),
        capital VARCHAR(255),
        atm_id INTEGER,
        atm_number VARCHAR(255),
        aml INTEGER);"""
)

conn.commit()

cur.execute("DROP TABLE IF EXISTS customer_dim;")
conn.commit()

cur.execute(
    """
create table customer_dim (
	customer_id INT,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
    email VARCHAR(50),
	gender VARCHAR(50),
	country_id INT
);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (1, 'Meredith', 'Scutchings', 'mscutchings0@scientificamerican.com', 'Female', 9);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (2, 'Alejandro', 'Irons', 'airons1@imdb.com', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (3, 'Gerrie', 'Bausor', 'gbausor2@drupal.org', 'Male', 7);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (4, 'Dasie', 'Conquer', 'dconquer3@cargocollective.com', 'Female', 2);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (5, 'Shirley', 'Really', 'sreally4@live.com', 'Female', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (6, 'Lynea', 'Giroldi', 'lgiroldi5@apple.com', 'Female', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (7, 'Sholom', 'Corrin', 'scorrin6@phpbb.com', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (8, 'Sioux', 'Cliffe', 'scliffe7@ucla.edu', 'Female', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (9, 'Mendie', 'Yeude', 'myeude8@livejournal.com', 'Non-binary', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (10, 'Siana', 'Endricci', 'sendricci9@sfgate.com', 'Female', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (11, 'John', 'Sizey', 'jsizeya@umich.edu', 'Male', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (12, 'Constantino', 'Haskell', 'chaskellb@dion.ne.jp', 'Male', 2);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (13, 'Eudora', 'Roll', 'erollc@theguardian.com', 'Female', 6);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (14, 'Bernardine', 'Harle', 'bharled@netvibes.com', 'Female', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (15, 'Rosco', 'Heintsch', 'rheintsche@pen.io', 'Male', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (16, 'Beverley', 'Dellenbrook', 'bdellenbrookf@answers.com', 'Polygender', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (17, 'Micheal', 'Conochie', 'mconochieg@skype.com', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (18, 'Casandra', 'Greenshiels', 'cgreenshielsh@fema.gov', 'Genderfluid', 7);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (19, 'Lexine', 'Deppen', 'ldeppeni@wikispaces.com', 'Female', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (20, 'Bendite', 'Pittford', 'bpittfordj@ehow.com', 'Female', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (21, 'Raye', 'Castagne', 'rcastagnek@zimbio.com', 'Female', 2);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (22, 'Brant', 'Shawley', 'bshawleyl@who.int', 'Male', 2);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (23, 'Gustave', 'Kubala', 'gkubalam@java.com', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (24, 'Egon', 'Tottem', 'etottemn@woothemes.com', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (25, 'Leela', 'Crowson', 'lcrowsono@mit.edu', 'Female', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (26, 'Kimberlyn', 'Bader', 'kbaderp@nytimes.com', 'Female', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (27, 'Mar', 'Cotillard', 'mcotillardq@shop-pro.jp', 'Male', 3);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (28, 'Alain', 'Capstick', 'acapstickr@reference.com', 'Male', 7);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (29, 'Nehemiah', 'Chiene', 'nchienes@state.tx.us', 'Male', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (30, 'Aguie', 'Harte', 'ahartet@nhs.uk', 'Male', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (31, 'Heath', 'Chasson', 'hchassonu@walmart.com', 'Male', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (32, 'Arlen', 'Juares', 'ajuaresv@phoca.cz', 'Female', 7);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (33, 'Antonina', 'McRobert', 'amcrobertw@delicious.com', 'Female', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (34, 'Berthe', 'Coltan', 'bcoltanx@java.com', 'Female', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (35, 'Bibby', 'Janiak', 'bjaniaky@businesswire.com', 'Female', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (36, 'Siegfried', 'Lunnon', 'slunnonz@harvard.edu', 'Male', 9);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (37, 'Levey', 'Galpen', 'lgalpen10@feedburner.com', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (38, 'Rubi', 'Grayson', 'rgrayson11@senate.gov', 'Female', 6);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (39, 'Pammi', 'Gudeman', 'pgudeman12@parallels.com', 'Female', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (40, 'Ethe', 'Coley', 'ecoley13@admin.ch', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (41, 'Billy', 'Cordie', 'bcordie14@google.cn', 'Female', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (42, 'Humbert', 'Gonnel', 'hgonnel15@google.ca', 'Male', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (43, 'Michele', 'Osbiston', 'mosbiston16@scribd.com', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (44, 'Guinevere', 'Fancy', 'gfancy17@woothemes.com', 'Female', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (45, 'Cassie', 'Rief', 'crief18@upenn.edu', 'Male', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (46, 'Kimbell', 'Heathorn', 'kheathorn19@miibeian.gov.cn', 'Genderqueer', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (47, 'Chrysler', 'Petrelli', 'cpetrelli1a@altervista.org', 'Non-binary', 6);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (48, 'Grantham', 'McClaren', 'gmcclaren1b@merriam-webster.com', 'Male', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (49, 'Arney', 'Gallant', 'agallant1c@nytimes.com', 'Non-binary', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (50, 'Adolf', 'Fardo', 'afardo1d@facebook.com', 'Male', 6);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (51, 'Donnajean', 'Bonny', 'dbonny1e@google.com', 'Female', 7);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (52, 'Virgilio', 'Dat', 'vdat1f@salon.com', 'Male', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (53, 'Kristine', 'Goodfield', 'kgoodfield1g@reference.com', 'Female', 2);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (54, 'Darlleen', 'Cleeve', 'dcleeve1h@163.com', 'Female', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (55, 'Modestia', 'Nussii', 'mnussii1i@cisco.com', 'Female', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (56, 'Val', 'De Coursey', 'vdecoursey1j@edublogs.org', 'Male', 3);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (57, 'Tressa', 'McTrustram', 'tmctrustram1k@netvibes.com', 'Female', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (58, 'Sapphira', 'Ashe', 'sashe1l@cargocollective.com', 'Female', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (59, 'Jeniece', 'Howlett', 'jhowlett1m@booking.com', 'Female', 6);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (60, 'Britni', 'Braker', 'bbraker1n@ca.gov', 'Female', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (61, 'Tremaine', 'Deniso', 'tdeniso1o@aol.com', 'Male', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (62, 'Sallyann', 'Cockroft', 'scockroft1p@creativecommons.org', 'Female', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (63, 'Kelli', 'Folley', 'kfolley1q@dailymotion.com', 'Female', 9);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (64, 'Kevyn', 'Tolefree', 'ktolefree1r@wisc.edu', 'Female', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (65, 'Byran', 'Flaverty', 'bflaverty1s@utexas.edu', 'Male', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (66, 'Joshia', 'Pyke', 'jpyke1t@ning.com', 'Male', 7);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (67, 'Nevil', 'Laurisch', 'nlaurisch1u@google.ru', 'Male', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (68, 'Minetta', 'Crowd', 'mcrowd1v@usgs.gov', 'Female', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (69, 'Bennie', 'Elcoux', 'belcoux1w@google.com.br', 'Female', 6);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (70, 'Fredra', 'De Stoop', 'fdestoop1x@smugmug.com', 'Female', 3);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (71, 'Artemis', 'Waddilove', 'awaddilove1y@biglobe.ne.jp', 'Male', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (72, 'Doris', 'Fuge', 'dfuge1z@hibu.com', 'Female', 2);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (73, 'Sara', 'Challender', 'schallender20@infoseek.co.jp', 'Female', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (74, 'Madella', 'MacGilrewy', 'mmacgilrewy21@360.cn', 'Female', 2);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (75, 'Jillie', 'Drinkhill', 'jdrinkhill22@jiathis.com', 'Female', 3);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (76, 'Beltran', 'Trobridge', 'btrobridge23@squidoo.com', 'Male', 6);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (77, 'Alis', 'Verrall', 'averrall24@answers.com', 'Agender', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (78, 'Thane', 'Jefferies', 'tjefferies25@google.co.uk', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (79, 'Fanni', 'Diviney', 'fdiviney26@tinyurl.com', 'Female', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (80, 'Godard', 'Vasilchikov', 'gvasilchikov27@posterous.com', 'Male', 3);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (81, 'Bogart', 'Sleeford', 'bsleeford28@thetimes.co.uk', 'Male', 9);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (82, 'Kurtis', 'Scotsbrook', 'kscotsbrook29@businessinsider.com', 'Male', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (83, 'Alexandr', 'Petters', 'apetters2a@altervista.org', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (84, 'Sheelagh', 'Anker', 'sanker2b@va.gov', 'Female', 8);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (85, 'Peggie', 'Furminger', 'pfurminger2c@google.co.uk', 'Female', 7);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (86, 'Jaquelyn', 'Furze', 'jfurze2d@dailymail.co.uk', 'Female', 1);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (87, 'Cecil', 'Harley', 'charley2e@squarespace.com', 'Female', 3);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (88, 'Jerad', 'Mcettrick', 'jmcettrick2f@cyberchimps.com', 'Male', 7);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (89, 'Winthrop', 'Aldcorn', 'waldcorn2g@adobe.com', 'Male', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (90, 'Ricard', 'Lambert', 'rlambert2h@pinterest.com', 'Male', 9);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (91, 'Sibyl', 'Wardroper', 'swardroper2i@aboutads.info', 'Male', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (92, 'Derick', 'Matfin', 'dmatfin2j@gmpg.org', 'Polygender', 3);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (93, 'Jerrylee', 'Ferraron', 'jferraron2k@chronoengine.com', 'Female', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (94, 'Leesa', 'Dillinton', 'ldillinton2l@wufoo.com', 'Female', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (95, 'Birgitta', 'Pendry', 'bpendry2m@google.it', 'Female', 3);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (96, 'Janean', 'Heinel', 'jheinel2n@marketwatch.com', 'Female', 6);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (97, 'Oswell', 'Dwyer', 'odwyer2o@cargocollective.com', 'Male', 5);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (98, 'Petronilla', 'Peyro', 'ppeyro2p@springer.com', 'Female', 4);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (99, 'Bank', 'Sherebrooke', 'bsherebrooke2q@springer.com', 'Male', 10);
insert into customer_dim (customer_id, first_name, last_name, email, gender, country_id) values (100, 'Sonni', 'Wightman', 'swightman2r@jigsy.com', 'Female', 3);
"""
)
conn.commit()

cur.execute("DROP TABLE IF EXISTS country;")
conn.commit()

cur.execute(
    """CREATE TABLE country (
    country_id INT,
    country VARCHAR(100));


Insert Into country (country_id, country) Values (1, 'Poland');  
Insert Into country (country_id, country) Values (2, 'Germany');  
Insert Into country (country_id, country) Values (3, 'France');  
Insert Into country (country_id, country) Values (4, 'Albania');  
Insert Into country (country_id, country) Values (5, 'Slovakia');  
Insert Into country (country_id, country) Values (6, 'Spain');  
Insert Into country (country_id, country) Values (7, 'Italy');  
Insert Into country (country_id, country) Values (8, 'Portugal');  
Insert Into country (country_id, country) Values (9, 'Belgium');  
Insert Into country (country_id, country) Values (10, 'Denmark');"""
)
conn.commit()


cur.execute("DROP TABLE IF EXISTS atm;")
conn.commit()

cur.execute(
    """CREATE TABLE atm (
    atm_id INT,
    atm_number VARCHAR(100),
    country_id INT);


Insert Into atm (atm_id, atm_number, country_id) Values (1, '14-936526-044367-5', 2);  
Insert Into atm (atm_id, atm_number, country_id) Values (2, '53-927924-767843-6', 3);  
Insert Into atm (atm_id, atm_number, country_id) Values (3, '37-069810-401198-9', 7);  
Insert Into atm (atm_id, atm_number, country_id) Values (4, '97-776180-446332-7', 6);  
Insert Into atm (atm_id, atm_number, country_id) Values (5, '31-896230-262583-3', 6);  
Insert Into atm (atm_id, atm_number, country_id) Values (6, '07-914661-382946-1', 3);  
Insert Into atm (atm_id, atm_number, country_id) Values (7, '76-115021-764852-8', 9);  
Insert Into atm (atm_id, atm_number, country_id) Values (8, '61-950502-476133-1', 10);  
Insert Into atm (atm_id, atm_number, country_id) Values (9, '32-679020-562334-4', 9);  
Insert Into atm (atm_id, atm_number, country_id) Values (10, '37-456918-870753-5', 1);     """
)
conn.commit()


cur.execute("DROP TABLE IF EXISTS location_national_capital;")
conn.commit()

cur.execute(
    """CREATE TABLE location_national_capital (
    country_id INT PRIMARY KEY,
    latitude DECIMAL(10, 7) NOT NULL,
    longitude DECIMAL(10, 7) NOT NULL);


    INSERT INTO location_national_capital (country_id, latitude, longitude)
    VALUES
    (1, 52.2297, 21.0122), -- Poland
    (2, 52.5200, 13.4050), -- Germany
    (3, 48.8566, 2.3522),  -- France
    (4, 41.3275, 19.8189), -- Albania
    (5, 48.1482, 17.1067), -- Slovakia
    (6, 40.4168, -3.7038), -- Spain
    (7, 41.9028, 12.4964), -- Italy
    (8, 38.7167, -9.1393), -- Portugal
    (9, 50.8503, 4.3517),  -- Belgium
    (10, 55.6761, 12.5683); -- Denmark
    """
)
conn.commit()

cur.close()
conn.close()
