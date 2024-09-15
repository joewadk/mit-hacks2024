DELETE FROM jawad;

INSERT INTO jawad (
    prescription_name, 
    raw_instruction, 
    expiration_date, 
    expected_time1, 
    expected_time2, 
    expected_time3
) 
VALUES 
    -- Known interaction: Warfarin and Aspirin
    ('Warfarin', 'Take once daily', '2025-12-31', '2025-12-31 08:00:00', NULL, NULL),
    ('Aspirin', 'Take twice daily', '2024-11-30', '2024-11-30 08:00:00', '2024-11-30 20:00:00', NULL),

    -- Other prescriptions
    ('Amoxicillin', 'Take every 6 hours', '2024-10-15', '2024-10-15 06:00:00', '2024-10-15 12:00:00', '2024-10-15 18:00:00'),
    ('Metformin', 'Take before meals', '2025-01-20', '2025-01-20 07:30:00', '2025-01-20 12:30:00', '2025-01-20 18:30:00'),
    ('Melatonin', 'Take at bedtime', '2024-09-25', '2024-09-25 22:00:00', NULL, NULL);

SELECT * FROM jawad;
