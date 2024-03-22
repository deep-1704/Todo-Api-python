use `Terabh_todo`;

INSERT INTO `user` (`username`, `password`) VALUES ('user1', 'user1');
INSERT INTO `user` (`username`, `password`) VALUES ('user2', 'user2');
INSERT INTO `user` (`username`, `password`) VALUES ('user3', 'user3');

INSERT INTO `task` (`username`, `description`, `status`) VALUES ('user1', 'task1', 0);
INSERT INTO `task` (`username`, `description`, `status`) VALUES ('user1', 'task2', 1);
INSERT INTO `task` (`username`, `description`, `status`) VALUES ('user2', 'task1', 0);
INSERT INTO `task` (`username`, `description`, `status`) VALUES ('user2', 'task2', 1);
INSERT INTO `task` (`username`, `description`, `status`) VALUES ('user3', 'task1', 0);
INSERT INTO `task` (`username`, `description`, `status`) VALUES ('user3', 'task2', 1);

