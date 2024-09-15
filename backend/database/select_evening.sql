SELECT prescription_name,raw_instruction
FROM jawad 
WHERE 
    (EXTRACT(HOUR FROM expected_time1) BETWEEN 17 AND 21)
    OR (EXTRACT(HOUR FROM expected_time2) BETWEEN 17 AND 21)
    OR (EXTRACT(HOUR FROM expected_time3) BETWEEN 17 AND 21);
