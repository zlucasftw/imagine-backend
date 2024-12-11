CREATE DATABASE imagine_backend;
USE imagine_backend;

CREATE TABLE banda (
    id_banda INT PRIMARY KEY AUTO_INCREMENT,
    nome_banda VARCHAR(100) NOT NULL,
    ano_estreia INT NOT NULL
    );

CREATE TABLE banda_historia (
    id_banda_historia INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    historia TEXT NOT NULL,
    id_banda INT NOT NULL
    );

CREATE TABLE banda_logo (
    id_banda_logo INT PRIMARY KEY AUTO_INCREMENT,
    logo_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(255) NOT NULL,
    id_banda INT NOT NULL
    );

CREATE TABLE banda_imagem (
    id_banda_imagem INT PRIMARY KEY AUTO_INCREMENT,
    imagem_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(255) NOT NULL,
    tipo_imagem VARCHAR(50) NOT NULL,
    id_banda INT NOT NULL
    );

CREATE TABLE banda_album (
    id_banda_album INT PRIMARY KEY AUTO_INCREMENT,
    id_banda INT NOT NULL,
    id_album INT NOT NULL
    );

CREATE TABLE album (
    id_album INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    ano_lancamento INT NOT NULL
    );

CREATE TABLE album_imagem (
    id_album_imagem INT PRIMARY KEY AUTO_INCREMENT,
    imagem_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(255) NOT NULL,
    id_album INT NOT NULL
    );
