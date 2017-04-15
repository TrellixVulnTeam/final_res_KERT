INSERT INTO User VALUES('yuxzhang','Yuxi','Zhang','zyx0520');

INSERT INTO Project(Topic,Abstract,Website,status)VALUES('Designing a Predictable Database','A Journey to Bring Back Performance Predictability to Databases','','Current');
INSERT INTO Project(Topic,Abstract,Website,status)VALUES('User Modeling','','https://en.wikipedia.org/wiki/User_modeling','Past');

INSERT INTO Publication(Publicationid,Pubname,Pubtime,Information,People)VALUES('1','Publishing Naive Bayesian Classifiers: Privacy without Accuracy Loss.','August 24-28, 2009',' In Proceedings of the 35th International Conference on Very Large Data Bases (PVLDB), Lyon, France,','Barzan Mozafari and Carlo Zaniolo.');
INSERT INTO Publication(Publicationid,Pubname,Pubtime,Information,People)VALUES('2',' On the Evolution of Wikipedia.','March 26-28, 2007','In Proceedings of the International Conference on Weblogs and Social Media (ICWSM), Boulder, Colorado, U.S.A.,','Rodrigo B. Almeida, Barzan Mozafari,');
INSERT INTO Publication(Publicationid,Pubname,Pubtime,Information,People)VALUES('3','Statistical Analysis of Latency Through Semantic Profiling.',' April 23-26, 2017',' In Proceedings of Proceedings of the European Conference on Computer Systems (EuroSys), Belgrade, Serbia,','Jiamin Huang, Barzan Mozafari and Thomas F. Wenisch.');
INSERT INTO Publication(Publicationid,Pubname,Pubtime,Information,People)VALUES('4','A Top-Down Approach to Achieving Performance Predictability in Database Systems.','May 14-19, 2017','In Proceedings of Proceedings of the ACM SIGMOD 2017 Conference, Chicago, IL, United States,','Jiamin Huang, Barzan Mozafari, Grant Schoenebeck, Thomas F. Wenisch.');

INSERT INTO Content(Paragraph)VALUES("Four decades of research on database systems has mostly focused on improving average raw performance. This competition for faster performance has, understandably, neglected predictability of our database management systems. However, as database systems have become more complex, their erratic and unpredictable performance has become a major challenge facing database users and administrators alike. With the increasing reliance of mission-critical business applications on their databases, maintaining high levels of database performance (i.e., service level guarantees) is now more important than ever. Cloud users find it challenging to provision and tune their database instances, due to the highly non-linear and unpredictable nature of today's databases. Even for deployed databases, performance tuning has become somewhat of a black art, rendering qualified database administrators a scare resource. In this project, we restore the missing virtue of predictability in the design of database systems. First, we quantify the major sources of uncertainty in a database in a principled manner. Then, by rethinking the traditional design of a database system, we architect a new generation of databases that treat predictability as a first class-citizen in their various stages of query processing, from physical design to memory management and query scheduling. Moreover, to accommodate existing database systems (which are not predictable by design), we provide effective tools and methodologies for predicting their performance more accurately. Building a predictable database in a bottom-up fashion and in a principled manner, offers great insight into improving existing database products and can instigate a radical shift in the way that future databases are designed and implemented.");
INSERT INTO Content(Paragraph)VALUES("The overall goal of the BlogoCenter project was to develop innovative technologies to build a system that will (1) continuously monitor, collect, and store personal Weblogs (or blogs) at a central location, (2) discover hidden structures and trends automatically from the blogs, and (3) make them easily accessible to general users. By making the new information on the blogs easy to discover and access, this project aimed at helping blogs realize their full potential for societal change as the grassroots media.");

INSERT INTO People(Peoplename)VALUES("Barzan Mozafari");
INSERT INTO People(Peoplename)VALUES("Grant Schoenebeck");
INSERT INTO People(Peoplename)VALUES("Jiamin Huang");
INSERT INTO People(Peoplename)VALUES("Thomas Wenisch");

INSERT INTO Picture(Pictureid,format)VALUES('user_modeling','jpg');
INSERT INTO Picture(Pictureid,format)VALUES('design_a_database','jpg');

INSERT INTO PeopleContain VALUES(1,1);
INSERT INTO PeopleContain VALUES(1,2);
INSERT INTO PeopleContain VALUES(1,3);
INSERT INTO PeopleContain VALUES(1,4);

INSERT INTO PublicationContain VALUES('2','1');
INSERT INTO PublicationContain VALUES('2','2');
INSERT INTO PublicationContain VALUES('1','3');
INSERT INTO PublicationContain VALUES('1','4');

INSERT INTO ContentContain VALUES(1,1);
INSERT INTO ContentContain VALUES(2,2);

INSERT INTO PictureContain VALUES(2,'user_modeling');
INSERT INTO PictureContain VALUES(1,'design_a_database');




