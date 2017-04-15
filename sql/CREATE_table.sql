CREATE TABLE Project(
  	Projectid  int primary key auto_increment,
  	Topic   varchar(100), 
  	Abstract varchar(300),
  	Website   varchar(50),
  	status varchar(20)
 );

CREATE TABLE Picture(
	Pictureid varchar(40) primary key,
	format  char(3) 
);

CREATE TABLE PictureContain(
	Projectid int,
	Pictureid varchar(40),
	primary key(Projectid,Pictureid)
);

CREATE TABLE Content(
	Contentid int primary key auto_increment,
	Paragraph  varchar(5000)
);

CREATE TABLE ContentContain(
	Projectid int,
	Contentid int,
	primary key(Projectid,Contentid),
	foreign key(Contentid) references Content(Contentid) on delete cascade,
	foreign key(Projectid) references Project(Projectid) on delete cascade
);

CREATE TABLE People (
	Peopleid  int primary key auto_increment,
	Peoplename varchar(30)
);
CREATE TABLE PeopleContain(
	Projectid int,
	Peopleid int,
	primary key(Projectid,Peopleid),
	foreign key(Peopleid) references People(Peopleid) on delete cascade,
	foreign key(Projectid) references Project(Projectid) on delete cascade
);

CREATE TABLE PublicationContain(
	Projectid int,
	Publicationid varchar(3),
	primary key(Projectid,Publicationid)

);


CREATE TABLE Publication(
	Publicationid varchar(3),
	Pubname   varchar(100) primary key,
	Pubtime   varchar(20),
	Information varchar(500),
	People   varchar(100)
);


CREATE TABLE User(
	username varchar(20) primary key,
	firstname varchar(20),
	lastname varchar(20),
	password varchar(20)
);

