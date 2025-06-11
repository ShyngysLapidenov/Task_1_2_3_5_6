DO $$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_database WHERE datname = 'registration_logs'
        ) THEN
        PERFORM dblink_exec('dbname-postgres', 'CREATE DATABASE registration_logs');
        END IF;
    EXCEPTION
        WHEN undefined_function THEN
            RAISE NOTICE 'dblink not available, skip CREATE DATABASE';
        WHEN OTHERS THEN
            RAISE NOTICE 'database already exists or error';
END
$$


