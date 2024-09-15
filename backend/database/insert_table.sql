delete from jawad;
INSERT INTO jawad (
    prescription_name, 
    raw_instruction, 
    expiration_date, 
    expected_time1, 
    expected_time2, 
    expected_time3
) 
VALUES 
    ('Prescription A', 'Take once daily', '2025-12-31', '2025-12-31', '2025-12-31', '2025-12-31'),
    ('Prescription B', 'Take twice daily', '2024-11-30', '2024-11-30', '2024-11-30', NULL),
    ('Prescription C', 'Take every 6 hours', '2024-10-15', '2024-10-15', '2024-10-15', '2024-10-15'),
    ('Prescription D', 'Take before meals', '2025-01-20', '2025-01-20', '2025-01-20', '2025-01-20'),
    ('Prescription E', 'Take at bedtime', '2024-09-25', '2024-09-25', NULL, NULL);
SELECT * FROM jawad;