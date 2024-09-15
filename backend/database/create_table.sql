DROP TABLE IF EXISTS jawad;

CREATE TABLE jawad (
    Prescription_name VARCHAR(255),
    Raw_instruction VARCHAR(255),
    expiration_date DATE,  
    Expected_time1 DATE,   
    Expected_time2 DATE,  
    Expected_time3 DATE,   
    PRIMARY KEY(Prescription_name)
);

SELECT * FROM jawad;
