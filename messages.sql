-- @block
CREATE TABLE recievedMessages(
    id int AUTO_INCREMENT PRIMARY KEY,
    temperature VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255)
);

-- @block
DROP TABLE recievedMessages;


-- @block
INSERT INTO recievedMessages (temperature, date, time)
VALUES (
    "4", "2026-06-17", CURTIME()
);



-- @block
SELECT * FROM recievedMessages;


-- @block 
DELETE FROM recievedMessages WHERE message = ""

