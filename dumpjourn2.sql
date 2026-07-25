BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "jtab" (
	"npp"	INTEGER,
	"dat"	TEXT,
	"numZak"	INTEGER,
	"phone"	TEXT,
	"nameZak"	TEXT,
	"descryption"	TEXT,
	"costSum"	REAL,
	"costYN"	BLOB,
	"prim"	TEXT,
	"End"	BLOB,
	PRIMARY KEY("npp" AUTOINCREMENT)
);
INSERT INTO "jtab" VALUES (1,'2024-01-26',3027,'+7 9604582244','Некто','Не влючается. Черный экран. Переустановить Windows',1200.0,0,'fhfghhfhgh',0);
INSERT INTO "jtab" VALUES (2,'2023-07-07',3028,'+7 9603845623','Кто-то','Не выключается',900.0,1,'',0);
INSERT INTO "jtab" VALUES (26,'2024-05-15',3089,'12345678','соплякин','что бы все',900.0,0,'',0);
INSERT INTO "jtab" VALUES (36,'2024-01-01',3225,'9192103778','jhkgfkhjkhjfg','HJFKHJGF jhmghjg',700.0,0,'fgdfgdfg',0);
INSERT INTO "jtab" VALUES (37,'2024-02-27',2345,'9192106773','xdfghdfhhfhg','GHJfhjgsfdjsdfhg
ППпрыаувропыалфопр
ываыв 56435435 ',400.0,0,'чсмчпвап',0);
INSERT INTO "jtab" VALUES (38,'2024-04-17',3067,'+79065774040','соплякин','ывапвап апапа ывапваыпывап вапвап',1500.0,1,'',0);
INSERT INTO "jtab" VALUES (39,'2024-04-14',3056,'1234567','uuuuuuu','eeeeeeeee',500.0,1,'',0);
INSERT INTO "jtab" VALUES (40,'2024-04-24',1111,'','rwererwer','klhblbkjbb',700.0,1,'',0);
INSERT INTO "jtab" VALUES (41,'2024-04-24',3333,'4566789','dfghfghdfgh','cvbncvbncvbncvbn bvnvcbn',1435.0,1,'',0);
INSERT INTO "jtab" VALUES (42,'2024-05-17',3334,'456456456','соплякин','ertyertyertyrt',3333.0,1,'',0);
INSERT INTO "jtab" VALUES (43,'2024-05-17',3335,'99999999','xcvbvcbxcvbcvxb','',222.0,0,'',0);
INSERT INTO "jtab" VALUES (44,'2024-05-17',3336,'456456456','ertyertyrtyrty','',345.0,0,'',0);
INSERT INTO "jtab" VALUES (45,'2024-05-19',3337,'88888888','oiuqwerfgbo',';sdjfkhg;dfglk ;lkshdfg;lkhsdfgkl',1400.0,0,'',0);
INSERT INTO "jtab" VALUES (46,'2024-05-05',3338,'','lkhgklhg','',100.0,0,'',0);
INSERT INTO "jtab" VALUES (47,'2024-08-04',3339,'','соплякин','',0.0,0,'',0);
INSERT INTO "jtab" VALUES (48,'2024-08-04',3340,'','','',0.0,1,'',1);
COMMIT;
