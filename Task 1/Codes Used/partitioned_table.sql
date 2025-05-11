CREATE TABLE bank_transactions (
    transaction_id SERIAL,
    transaction_date DATE NOT NULL,
    domain VARCHAR(20) NOT NULL,
    location VARCHAR(50) NOT NULL,
    value INTEGER NOT NULL,
    transaction_count INTEGER NOT NULL
) PARTITION BY RANGE (transaction_date);
