-- @block
CREATE TABLE recievedMessages(
    id int AUTO_INCREMENT PRIMARY KEY,
    tempreture VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255)
);

-- @block
DROP TABLE recievedMessages;


-- @block
INSERT INTO recievedMessages (tempreture, date, time)
VALUES (
    "hello", CURDATE(), CURTIME()
);



-- @block
SELECT * FROM recievedMessages;


-- @block 
DELETE FROM recievedMessages WHERE message = ""

