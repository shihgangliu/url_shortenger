CREATE TABLE `url_map` (
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `original_url` VARCHAR(255) NOT NULL,
    `short_url` VARCHAR(5) NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `expires_at` TIMESTAMP NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
