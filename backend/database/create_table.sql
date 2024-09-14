DROP TABLE IF EXISTS pub;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE pub (
    uid UUID NOT NULL DEFAULT uuid_generate_v4(),
    f_name VARCHAR(255),
    l_name VARCHAR(255),
    rx_name VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Adding datetime parameter
    PRIMARY KEY (uid)
);

SELECT * FROM pub;