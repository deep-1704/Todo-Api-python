use `Terabh_todo`;

create table user(
	`username` varchar(50) not null,
    `password` varchar(50) not null,
    
    primary key(`username`)
);

create table task(
	`id` int not null,
    `username` varchar(50),
    `description` varchar(100),
    `status` boolean,
    
    primary key(`id`),
    FOREIGN KEY (`username`) REFERENCES `user`(`username`)
);