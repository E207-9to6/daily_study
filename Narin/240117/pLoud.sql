CREATE TABLE `Room` (
	`room_number`	VARCHAR(255)	NOT NULL,
	`user_id`	VARCHAR(255)	NOT NULL,
	`category_id`	VARCHAR(255)	NOT NULL,
	`name`	VARCHAR(255)	NULL,
	`public`	BOOLEAN	NULL,
	`password`	VARCHAR(255)	NULL,
	`study_start`	BOOLEAN	NULL,
	`Field`	VARCHAR(255)	NULL,
	`max_people`	VARCHAR(255)	NULL
);

CREATE TABLE `User` (
	`user_id`	VARCHAR(255)	NOT NULL,
	`name`	VARCHAR(255)	NULL,
	`nickname`	VARCHAR(255)	NULL,
	`password`	VARCHAR(255)	NULL,
	`profile_img`	VARCHAR(255)	NULL,
	`email`	VARCHAR(255)	NULL,
	`token`	VARCHAR(255)	NULL,
	`birth_year`	VARCHAR(255)	NULL,
	`complain_count`	VARCHAR(255)	NULL,
	`restriction`	VARCHAR(255)	NULL
);

CREATE TABLE `Script` (
	`script_id`	AUTO_INCREMENT	NOT NULL,
	`speech_id`	VARCHAR(255)	NOT NULL,
	`user_id`	VARCHAR(255)	NOT NULL,
	`category_id`	VARCHAR(255)	NOT NULL,
	`title`	VARCHAR(255)	NULL,
	`video_url`	VARCHAR(255)	NULL,
	`content`	VARCHAR(255)	NULL,
	`category`	VARCHAR(255)	NULL
);

CREATE TABLE `Complain` (
	`complain_id`	VARCHAR(255)	NOT NULL,
	`black_user`	VARCHAR(255)	NOT NULL,
	`title`	VARCHAR(255)	NULL,
	`content`	VARCHAR(255)	NULL,
	`time`	VARCHAR(255)	NULL,
	`restriction`	BOOLEAN	NULL
);

CREATE TABLE `Articles` (
	`article_id`	VARCHAR(255)	NOT NULL,
	`user_id`	VARCHAR(255)	NOT NULL,
	`title`	VARCHAR(255)	NULL,
	`content`	VARCHAR(255)	NULL,
	`video_url`	VARCHAR(255)	NULL,
	`time`	VARCHAR(255)	NULL
);

CREATE TABLE `Comment` (
	`comment_id`	VARCHAR(255)	NOT NULL,
	`article_id`	VARCHAR(255)	NOT NULL,
	`user_id`	VARCHAR(255)	NOT NULL,
	`time`	VARCHAR(255)	NULL,
	`content`	VARCHAR(255)	NULL
);

CREATE TABLE `Feedback` (
	`feedback_id`	VARCHAR(255)	NOT NULL,
	`writer`	VARCHAR(255)	NOT NULL,
	`speech_id`	VARCHAR(255)	NOT NULL,
	`user_id2`	VARCHAR(255)	NOT NULL,
	`content`	VARCHAR(255)	NULL,
	`time`	VARCHAR(255)	NULL
);

CREATE TABLE `Score` (
	`speech_id`	VARCHAR(255)	NOT NULL,
	`user_id`	VARCHAR(255)	NOT NULL,
	`clarity`	VARCHAR(255)	NOT NULL,
	`speed`	VARCHAR(255)	NULL,
	`volume`	VARCHAR(255)	NULL,
	`eye_contact`	VARCHAR(255)	NULL,
	`grade`	VARCHAR(255)	NULL
);

CREATE TABLE `Category` (
	`category_id`	VARCHAR(255)	NOT NULL,
	`title`	VARCHAR(255)	NULL
);

CREATE TABLE `Speech` (
	`speech_id`	VARCHAR(255)	NOT NULL,
	`user_id`	VARCHAR(255)	NOT NULL,
	`category_id`	VARCHAR(255)	NOT NULL,
	`personal`	BOOLEAN	NULL,
	`rec_at`	VARCHAR(255)	NULL
);

CREATE TABLE `Video` (
	`video_id`	VARCHAR(255)	NOT NULL,
	`speech_id`	VARCHAR(255)	NOT NULL,
	`user_id`	VARCHAR(255)	NOT NULL,
	`Key`	VARCHAR(255)	NOT NULL,
	`video_url`	VARCHAR(255)	NULL,
	`rec_time`	VARCHAR(255)	NULL
);

CREATE TABLE `Hearts` (
	`Key`	VARCHAR(255)	NOT NULL
);

CREATE TABLE `ScriptCategory` (
	`category_id`	VARCHAR(255)	NOT NULL,
	`title`	VARCHAR(255)	NULL
);

ALTER TABLE `Room` ADD CONSTRAINT `PK_ROOM` PRIMARY KEY (
	`room_number`,
	`user_id`,
	`category_id`
);

ALTER TABLE `User` ADD CONSTRAINT `PK_USER` PRIMARY KEY (
	`user_id`
);

ALTER TABLE `Script` ADD CONSTRAINT `PK_SCRIPT` PRIMARY KEY (
	`script_id`,
	`speech_id`,
	`user_id`,
	`category_id`
);

ALTER TABLE `Complain` ADD CONSTRAINT `PK_COMPLAIN` PRIMARY KEY (
	`complain_id`,
	`black_user`
);

ALTER TABLE `Articles` ADD CONSTRAINT `PK_ARTICLES` PRIMARY KEY (
	`article_id`,
	`user_id`
);

ALTER TABLE `Comment` ADD CONSTRAINT `PK_COMMENT` PRIMARY KEY (
	`comment_id`,
	`article_id`,
	`user_id`
);

ALTER TABLE `Feedback` ADD CONSTRAINT `PK_FEEDBACK` PRIMARY KEY (
	`feedback_id`,
	`writer`,
	`speech_id`,
	`user_id2`
);

ALTER TABLE `Score` ADD CONSTRAINT `PK_SCORE` PRIMARY KEY (
	`speech_id`,
	`user_id`
);

ALTER TABLE `Category` ADD CONSTRAINT `PK_CATEGORY` PRIMARY KEY (
	`category_id`
);

ALTER TABLE `Speech` ADD CONSTRAINT `PK_SPEECH` PRIMARY KEY (
	`speech_id`,
	`user_id`,
	`category_id`
);

ALTER TABLE `Video` ADD CONSTRAINT `PK_VIDEO` PRIMARY KEY (
	`video_id`,
	`speech_id`,
	`user_id`,
	`Key`
);

ALTER TABLE `Hearts` ADD CONSTRAINT `PK_HEARTS` PRIMARY KEY (
	`Key`
);

ALTER TABLE `ScriptCategory` ADD CONSTRAINT `PK_SCRIPTCATEGORY` PRIMARY KEY (
	`category_id`
);

ALTER TABLE `Room` ADD CONSTRAINT `FK_User_TO_Room_1` FOREIGN KEY (
	`user_id`
)
REFERENCES `User` (
	`user_id`
);

ALTER TABLE `Room` ADD CONSTRAINT `FK_Category_TO_Room_1` FOREIGN KEY (
	`category_id`
)
REFERENCES `Category` (
	`category_id`
);

ALTER TABLE `Script` ADD CONSTRAINT `FK_Speech_TO_Script_1` FOREIGN KEY (
	`speech_id`
)
REFERENCES `Speech` (
	`speech_id`
);

ALTER TABLE `Script` ADD CONSTRAINT `FK_Speech_TO_Script_2` FOREIGN KEY (
	`user_id`
)
REFERENCES `Speech` (
	`user_id`
);

ALTER TABLE `Script` ADD CONSTRAINT `FK_ScriptCategory_TO_Script_1` FOREIGN KEY (
	`category_id`
)
REFERENCES `ScriptCategory` (
	`category_id`
);

ALTER TABLE `Complain` ADD CONSTRAINT `FK_User_TO_Complain_1` FOREIGN KEY (
	`black_user`
)
REFERENCES `User` (
	`user_id`
);

ALTER TABLE `Articles` ADD CONSTRAINT `FK_User_TO_Articles_1` FOREIGN KEY (
	`user_id`
)
REFERENCES `User` (
	`user_id`
);

ALTER TABLE `Comment` ADD CONSTRAINT `FK_Articles_TO_Comment_1` FOREIGN KEY (
	`article_id`
)
REFERENCES `Articles` (
	`article_id`
);

ALTER TABLE `Comment` ADD CONSTRAINT `FK_User_TO_Comment_1` FOREIGN KEY (
	`user_id`
)
REFERENCES `User` (
	`user_id`
);

ALTER TABLE `Feedback` ADD CONSTRAINT `FK_User_TO_Feedback_1` FOREIGN KEY (
	`writer`
)
REFERENCES `User` (
	`user_id`
);

ALTER TABLE `Feedback` ADD CONSTRAINT `FK_Speech_TO_Feedback_1` FOREIGN KEY (
	`speech_id`
)
REFERENCES `Speech` (
	`speech_id`
);

ALTER TABLE `Feedback` ADD CONSTRAINT `FK_Speech_TO_Feedback_2` FOREIGN KEY (
	`user_id2`
)
REFERENCES `Speech` (
	`user_id`
);

ALTER TABLE `Score` ADD CONSTRAINT `FK_Speech_TO_Score_1` FOREIGN KEY (
	`speech_id`
)
REFERENCES `Speech` (
	`speech_id`
);

ALTER TABLE `Score` ADD CONSTRAINT `FK_Speech_TO_Score_2` FOREIGN KEY (
	`user_id`
)
REFERENCES `Speech` (
	`user_id`
);

ALTER TABLE `Speech` ADD CONSTRAINT `FK_User_TO_Speech_1` FOREIGN KEY (
	`user_id`
)
REFERENCES `User` (
	`user_id`
);

ALTER TABLE `Speech` ADD CONSTRAINT `FK_Category_TO_Speech_1` FOREIGN KEY (
	`category_id`
)
REFERENCES `Category` (
	`category_id`
);

ALTER TABLE `Video` ADD CONSTRAINT `FK_Speech_TO_Video_1` FOREIGN KEY (
	`speech_id`
)
REFERENCES `Speech` (
	`speech_id`
);

ALTER TABLE `Video` ADD CONSTRAINT `FK_Speech_TO_Video_2` FOREIGN KEY (
	`user_id`
)
REFERENCES `Speech` (
	`user_id`
);

ALTER TABLE `Video` ADD CONSTRAINT `FK_Speech_TO_Video_3` FOREIGN KEY (
	`Key`
)
REFERENCES `Speech` (
	`category_id`
);

