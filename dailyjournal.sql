CREATE TABLE `Moods` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`	TEXT NOT NULL
);

CREATE TABLE `Tags` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`subject`	TEXT NOT NULL
);

CREATE TABLE `Instructors` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`first_name`	TEXT NOT NULL,
	`last_name`	TEXT NOT NULL
);

CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`concept`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
	`mood_id`	TEXT NOT NULL,
	`instructor_id`	TEXT NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
    FOREIGN KEY(`instructor_id`) REFERENCES `Instructors`(`id`)
);

CREATE TABLE `Entries_Tags` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`entry_id`	TEXT NOT NULL,
	`tag_id`	TEXT NOT NULL,
    FOREIGN KEY(`entry_id`) REFERENCES `Entries`(`id`)
    FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);



INSERT INTO `Moods` VALUES (null, "Focused");
INSERT INTO `Moods` VALUES (null, "Happy");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Elated");
INSERT INTO `Moods` VALUES (null, "Despair");

INSERT INTO `Tags` VALUES (null, "Python!");
INSERT INTO `Tags` VALUES (null, "React!");
INSERT INTO `Tags` VALUES (null, "SQL");
INSERT INTO `Tags` VALUES (null, "Back End");
INSERT INTO `Tags` VALUES (null, "Front End");
INSERT INTO `Tags` VALUES (null, "Javascript");

INSERT INTO `Instructors` VALUES (null, "Steve", "Brownlee");
INSERT INTO `Instructors` VALUES (null, "Joe", "Sheperd");
INSERT INTO `Instructors` VALUES (null, "Jack", "Parsons");
INSERT INTO `Instructors` VALUES (null, "Mo", "Silvera");
INSERT INTO `Instructors` VALUES (null, "Spencer", "Pruett");
INSERT INTO `Instructors` VALUES (null, "Kristen", "Norris");
INSERT INTO `Instructors` VALUES (null, "James", "Avery");

INSERT INTO `Entries` VALUES (null, "2020-08-21T10:50", "effect hooks", "today we learned hooks", 1, 1);
INSERT INTO `Entries` VALUES (null, "2020-08-21T10:41", "State managemnent", "how many states and who manages them", 3, 2);
INSERT INTO `Entries` VALUES (null, "2020-08-24T20:38", "Python", "what is whitespace", 2, 3);
INSERT INTO `Entries` VALUES (null, "2020-08-21T15:13", "The Internet", "What it is and what it does", 5, 3);