-- Add a new column named rank_id to the rl table
ALTER TABLE rl ADD COLUMN rank_id INTEGER;

-- Update rank_id values based on rank names
UPDATE rl SET rank_id = 1 WHERE rank = 'Bronze 1';
UPDATE rl SET rank_id = 6 WHERE rank = 'Bronze 2';
UPDATE rl SET rank_id = 3 WHERE rank = 'Bronze 3';
UPDATE rl SET rank_id = 44 WHERE rank = 'Silver 1';
UPDATE rl SET rank_id = 96 WHERE rank = 'Silver 2';
UPDATE rl SET rank_id = 22 WHERE rank = 'Silver 3';
UPDATE rl SET rank_id = 11 WHERE rank = 'Gold 1';
UPDATE rl SET rank_id = 19 WHERE rank = 'Gold 2';
UPDATE rl SET rank_id = 10 WHERE rank = 'Gold 3';
UPDATE rl SET rank_id = 86 WHERE rank = 'Platinum 1';
UPDATE rl SET rank_id = 69 WHERE rank = 'Platinum 2';
UPDATE rl SET rank_id = 77 WHERE rank = 'Platinum 3';
UPDATE rl SET rank_id = 76 WHERE rank = 'Diamond 1';
UPDATE rl SET rank_id = 32 WHERE rank = 'Diamond 2';
UPDATE rl SET rank_id = 12 WHERE rank = 'Diamond 3';
UPDATE rl SET rank_id = 90 WHERE rank = 'Champion 1';
UPDATE rl SET rank_id = 60 WHERE rank = 'Champion 2';
UPDATE rl SET rank_id = 40 WHERE rank = 'Champion 3';
UPDATE rl SET rank_id = 35 WHERE rank = 'Grand Champion 1';
UPDATE rl SET rank_id = 67 WHERE rank = 'Grand Champion 2';
UPDATE rl SET rank_id = 68 WHERE rank = 'Grand Champion 3';
UPDATE rl SET rank_id = 99 WHERE rank = 'Supersonic Legend';

-- Commit changes
COMMIT;
