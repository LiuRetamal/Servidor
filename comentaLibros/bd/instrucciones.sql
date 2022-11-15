CREATE USER 'comentaLibros'@'localhost' IDENTIFIED VIA mysql_native_password USING '***';
GRANT USAGE ON *.* TO 'comentaLibros'@'localhost' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
CREATE DATABASE IF NOT EXISTS `comentaLibros`;
GRANT ALL PRIVILEGES ON `comentaLibros`.* TO 'comentaLibros'@'localhost';

CREATE TABLE roles{
    id int NOT NULL AUTO_INCREMENT,
    descripcion varchar(255),
    PRIMARY KEY (id)
};
CREATE TABLE usuarios{
    id int NOT NULL AUTO_INCREMENT,
    usuario varchar(255) UNIQUE NOT NULL,
    passwd varchar(600) NOT NULL,
    mail varchar(255),
    rollId int,
    coki varchar(600) NOT NULL,
    FOREIGN KEY (rollId) REFERENCES roles(id),
    PRIMARY KEY (id)
};
CREATE TABLE comentarios (
    id INT NOT NULL AUTO_INCREMENT,
    titulo varchar(255) NOT NULL,
    autor varchar(255) NOT NULL,
    comentario varchar(3000) NOT NULL,
    usuarioId INT NOT NULL,
    imagen varchar(255),
    PRIMARY KEY (id),
    FOREIGN KEY (usuarioId) REFERENCES usuarios(id)
);

