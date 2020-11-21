CREATE TABLE `equacao` (
    `id` INT(11) PRIMARY KEY AUTO_INCREMENT,
    `area` DECIMAL NOT NULL,
    `created` DATETIME DEFAULT CURRENT_TIMESTAMP()
);

-- INSERT INTO `quote` (`quote`, `quote_by`, `added_by`)
-- VALUES ('Most software today is very much like an Egyptian pyramid with millions of bricks piled on top of each other, with no structural integrity, but just done by brute force and thousands of slaves.', 'Allan Kay', 'Sam');