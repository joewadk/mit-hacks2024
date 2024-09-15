DROP TABLE IF EXISTS jawad;

CREATE TABLE jawad (
    Prescription_name VARCHAR(255),
    Raw_instruction VARCHAR(255),
    expiration_date DATE,  
    Expected_time1 TIMESTAMP,   
    Expected_time2 TIMESTAMP,  
    Expected_time3 TIMESTAMP,   
    PRIMARY KEY(Prescription_name)
);

SELECT * FROM jawad;
