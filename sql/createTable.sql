create table student(
  sno   char(3),
  sname varchar(8),
  ssex  char(2),
  sage  smallint,
  sdept char(2),
  constraint PK_student primary key(sno),
  constraint CK_ssex    check(ssex='ÄĞ' or ssex='Å®'),
  constraint CK_sage    check(sage>=15 and sage<=60)
)
create table course(
  cno     char(3),
  cname   varchar(20),
  cpno    char(3),
  ccredit int,
  constraint PK_course primary key(cno),
  constraint FK_course_course foreign key(cpno) references course(cno)
)
create table sc(
  sno   char(3),
  cno   char(3), 
  grade int,
  constraint PK_sc primary key(sno,cno),
  constraint FK_sc_student foreign key(sno) references student(sno),
  constraint FK_sc_course  foreign key(cno) references course(cno),
  constraint CK_grade check(grade>=0 and grade<=100)
)

create table student1(
  sno   char(3),
  sname varchar(8),
  ssex  char(2),
  sage  smallint,
  sdept char(2),
  primary key(sno),
  check(ssex='ÄĞ' or ssex='Å®'),
  check(sage>=15 and sage<=60)
)

create table student2(
  sno   char(3) primary key(sno),
  sname varchar(8),
  ssex  char(2) check(ssex='ÄĞ' or ssex='Å®'),
  sage  smallint check(sage>=15 and sage<=60),
  sdept char(2),
)

create table sc(
  sno   char(3) foreign key(sno) references student(sno),
  cno   char(3) foreign key(cno) references course(cno), 
  grade int check(grade>=0 and grade<=100),
  constraint PK_sc primary key(sno,cno)
)