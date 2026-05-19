-- @block
CREATE TABLE recievedMessages(
    id int AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255)
);

-- @block
DROP TABLE recievedMessages;


-- @block
INSERT INTO recievedmessages (message)
VALUES (
    "hello"
);


-- @block
SELECT * FROM recievedMessages;

-- @block 
DELETE FROM recievedMessages WHERE message = ""
