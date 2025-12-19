INSERT INTO customers VALUES
('C001', '2025-12-01', 'Ravi', 'Kumar', 50000, 'B1', true, 'Unpaid'),
('C002', '2025-12-01', 'Anita', 'Shah', 75000, 'B2', false, 'Partial'),
('C003', '2025-12-01', 'Vikas', 'Mehta', 30000, 'B1', true, 'Unpaid');

INSERT INTO call_logs VALUES
(gen_random_uuid(), 'C001', CURRENT_DATE, true, true, 5000),
(gen_random_uuid(), 'C001', CURRENT_DATE - 1, false, false, NULL),
(gen_random_uuid(), 'C002', CURRENT_DATE, true, false, NULL),
(gen_random_uuid(), 'C003', CURRENT_DATE, true, true, 3000);
