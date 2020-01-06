CREATE TABLE `quote` (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `quote` VARCHAR(512) NOT NULL,
    `quote_by` VARCHAR(100),
    `added_by` VARCHAR(100),
    `created` DATETIME DEFAULT CURRENT_TIMESTAMP(),
    `updated` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP()
);

INSERT INTO `quote` (`quote`, `quote_by`, `added_by`)
VALUES ('Most software today is very much like an Egyptian pyramid with millions of bricks piled on top of each other, with no structural integrity, but just done by brute force and thousands of slaves.', 'Allan Kay', 'Sam');