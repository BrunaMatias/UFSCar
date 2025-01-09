create table Aluno(
nome varchar(30),
RA integer,
idade integer, 
dataNasc date,
constraint pkNome primary key (nome),
constraint pkRa unique (RA)
);

create table professor(
nomeProf varchar(70),
NFunc integer,
idade integer,
titulacao varchar(70),
constraint pkNomeProf primary key (nomeProf),
constraint pkNFunc unique (NFunc)
);

create table Disciplina(
sigla integer,
nome varchar(40),
nCred integer, 
professor integer,
livro varchar(70),
constraint pkSigla primary key (sigla),
constraint fkProfessor foreign key (professor) references Professor(NFunc)
);

create table turma(
sigla integer, 
numero integer,
nAlunos integer,
constraint fkSigla foreign key (sigla) references Disciplina(sigla),
constraint pkTurma primary key (sigla, numero)
);

create table Matricula(
sigla integer,
numero integer,
aluno integer, 
ano integer,
nota float,
constraint fkTurmaSiglaNumero foreign key (sigla, numero) references Turma(sigla, numero),
constraint fkAluno foreign key (aluno) references Aluno(RA)
)

