use tmi;
/*CREATE TABLE `User` (
    userID CHAR(14),
    passwd VARCHAR(100),
    lastName VARCHAR(15),
    firstName VARCHAR(15),
    address VARCHAR(50),
    city VARCHAR(15),
    state VARCHAR(15),
    email VARCHAR(50),
    rating REAL,
    userType ENUM('user', 'employee', 'manager', 'company'),
    PRIMARY KEY (userID)
);

CREATE TABLE Preferences (
    userID CHAR(14),
    preference VARCHAR(15),
    PRIMARY KEY (userID , preference),
    FOREIGN KEY (userID)
        REFERENCES `User` (userID)
);
CREATE TABLE uAccount (
    accountNo INT,
    Aowner CHAR(14),
    creationDate DATE,
    cardNo INT,
    PRIMARY KEY (accountNo , Aowner),
    FOREIGN KEY (Aowner)
        REFERENCES `User` (userID)
);
CREATE TABLE Friend (
    firstUser CHAR(14),
    secondUser CHAR(14),
    PRIMARY KEY (firstUser , secondUser),
    FOREIGN KEY (firstUser)
        REFERENCES `User` (userID),
    FOREIGN KEY (secondUser)
        REFERENCES `User` (userID)
);
CREATE TABLE fGroup (
    groupID INT AUTO_INCREMENT,
    groupName VARCHAR(25),
    groupType ENUM('club', 'organization', 'other'),
    Gstatus ENUM('closed', 'public', 'secret'),
    Gowner CHAR(14),
    PRIMARY KEY (groupID),
    FOREIGN KEY (Gowner)
        REFERENCES `User` (userID)
);
CREATE TABLE Member (
    groupID INT,
    membership ENUM('admin', 'user'),
    userID CHAR(14),
    PRIMARY KEY (groupID , userID),
    FOREIGN KEY (userID)
        REFERENCES `User` (userID)
        ON DELETE CASCADE,
    FOREIGN KEY (groupID)
        REFERENCES fGroup (groupID)
        ON DELETE CASCADE
);
CREATE TABLE `Page` (
    pageID INT AUTO_INCREMENT,
    Powner CHAR(14),
    fGroup INT,
    postCount INT,
    PRIMARY KEY (pageID),
    FOREIGN KEY (Powner)
        REFERENCES `User` (userID)
        ON DELETE CASCADE,
    FOREIGN KEY (fGroup)
        REFERENCES fGroup (groupID)
        ON DELETE CASCADE
);
CREATE TABLE Post (
    postID INT AUTO_INCREMENT,
    `owner` CHAR(14) NOT NULL,
    pageID INT,
    postDate DATETIME,
    content TEXT,
    commentCount INT,
    likesCount INT,
    PRIMARY KEY (postID),
    FOREIGN KEY (`owner`)
        REFERENCES `User` (userID),
    FOREIGN KEY (pageID)
        REFERENCES `Page` (pageID)
);
CREATE TABLE `Comment` (
    commentID INT AUTO_INCREMENT,
    postID INT,
    created DATE,
    content TEXT,
    author CHAR(14),
    likesCount INT,
    PRIMARY KEY (commentID),
    FOREIGN KEY (postID)
        REFERENCES Post (postID)
        ON DELETE CASCADE,
    FOREIGN KEY (author)
        REFERENCES `User` (userID)
        ON DELETE CASCADE
);

CREATE TABLE Message (
    MessageId INTEGER AUTO_INCREMENT NOT NULL,
    MDate DATETIME NOT NULL,
    MSubject VARCHAR(100),
    MContent TEXT,
    MSenderId CHAR(14) NOT NULL,
    MReceiverId CHAR(14) NOT NULL,
    PRIMARY KEY (MessageId),
    FOREIGN KEY (MSenderId)
        REFERENCES `User` (userId)
        ON DELETE NO ACTION,
    FOREIGN KEY (MReceiverId)
        REFERENCES `User` (userId)
        ON DELETE NO ACTION
);
CREATE TABLE LikePost (
    PostId INTEGER,
    UserId CHAR(14) NOT NULL,
    PRIMARY KEY (PostId , UserId),
    FOREIGN KEY (PostId)
        REFERENCES Post (PostID)
        ON DELETE CASCADE,
    FOREIGN KEY (UserId)
        REFERENCES `User` (userID)
        ON DELETE NO ACTION
);

CREATE TABLE LikeComment (
    CommentId INTEGER,
    UserId CHAR(14) NOT NULL,
    PRIMARY KEY (CommentId , UserId),
    FOREIGN KEY (CommentId)
        REFERENCES Comment (CommentID)
        ON DELETE NO ACTION,
    FOREIGN KEY (UserId)
        REFERENCES `User` (userID)
        ON DELETE NO ACTION
);


CREATE TABLE Employee (
    SSN INT NOT NULL,
    UserID CHAR(14) NOT NULL,
    FirstName CHAR(50),
    LastName CHAR(50),
    StartDate DATE NOT NULL,
    Address CHAR(70),
    ZipCode INT,
    State CHAR(50),
    Telephone INT,
    HourlyRate DOUBLE NOT NULL,
    CName CHAR(50) NOT NULL,
    PRIMARY KEY (SSN)
);


CREATE TABLE StoreAccounts (
    userID CHAR(14),
    CompanyName CHAR(50),
    AccountNo INT,
    CreditCardNumber INT,
    PRIMARY KEY (CreditCardNumber),
    FOREIGN KEY (userID)
        REFERENCES `User` (userID)
);

CREATE TABLE Advertisements (
    AdvertisementID INTEGER AUTO_INCREMENT NOT NULL,
    EmployeeID INT NOT NULL,
    MerchandiseType CHAR(50),
    DatePublished DATE,
    Company CHAR(50),
    ItemName CHAR(70),
    UnitPrice DOUBLE,
    NoAvailableUnits INT,
    CHECK (MERCHANDISETYPE(VALUE IN ('Staple' , 'Assortment', 'Fashion', 'Seasonal'))),
    PRIMARY KEY (AdvertisementID),
    FOREIGN KEY (EmployeeID)
        REFERENCES Employee (SSN)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Sales (
    TransactionID INT AUTO_INCREMENT NOT NULL,
    DatePurchase DATE,
    AdvertisementID INT,
    NumberofUnits INT,
    TotalPrice DOUBLE,
    AccountNumber INT,
    UserName CHAR(14),
    PRIMARY KEY (TransactionID),
    FOREIGN KEY(UserName) REFERENCES `User`(userID),
    FOREIGN KEY (AdvertisementID)
        REFERENCES Advertisements (AdvertisementID)
        ON UPDATE CASCADE ON DELETE CASCADE
);

DELIMITER //

CREATE PROCEDURE login(
    userID CHAR(14),
    passwd VARCHAR(54)
)
BEGIN
    SELECT *
    FROM `User`
    WHERE(`User`.userID = userID AND `User`.passwd = passwd);
    
END//

CREATE PROCEDURE registerUser(
 	userID CHAR(14),
    passwd VARCHAR(100),
	lastName VARCHAR(15),
	firstName VARCHAR(15),
	address VARCHAR(50),
	city VARCHAR(15),
	state VARCHAR(15),
	email VARCHAR(50),
	rating REAL,
	userType ENUM('user', 'employee', 'manager', 'company')
 )
 BEGIN
    INSERT INTO `User`(userID,passwd,lastname,firstname,address,city,state,
		email,rating,userType)
    VALUES (userID,passwd,lastName,firstName,
		address,city,state,email,rating,userType);
	INSERT INTO `Page`(Powner, postCount)
    VALUES(userID,0);
 END//

 CREATE PROCEDURE addPreferences(
     userID CHAR(14),
     preference VARCHAR(15)
 )

BEGIN
    INSERT INTO Preferences
    VALUES (userID, preference);
END//

CREATE PROCEDURE createGroup(
	groupName VARCHAR(25),
	groupType ENUM('club', 'organization', 'other'),
	Gstatus ENUM('closed', 'public', 'secret'),
	Gowner CHAR(14)
)
BEGIN
	declare t int;
    INSERT INTO fGroup(groupName, groupType, Gstatus, Gowner)
    VALUES (groupName, groupType, Gstatus, Gowner);
    select last_insert_id() into t;
    insert into `Page`(fGroup, postCount)
    values(t,0);
    insert into Member(groupID,membership,userId)
    values(t,'admin',Gowner);
END//

CREATE PROCEDURE searchUser(
    firstName VARCHAR(15),
    lastName VARCHAR(15),
    userID CHAR(14)
)
BEGIN
    SELECT * 
    FROM `User` U
    WHERE(userID = U.userID
    OR (U.firstName like firstName AND U.lastName like lastName));
END//

CREATE PROCEDURE ownerMakePost(
	`owner` CHAR(14),
	content TEXT
)
BEGIN
	declare t datetime;
    declare pageID int;
    select now() into t;
    select P.pageID into pageID from page P where P.Powner = `owner`;
    INSERT INTO Post (`owner`,pageID,postDate,content,commentCount,likesCount)
    VALUES (`owner`,  pageID,  t, 
		content, 0, 0);
    UPDATE `Page` 
    SET postCount = postCount + 1
    WHERE (`Page`.pageID = pageID);
END//

CREATE PROCEDURE ownerCommentPost(
	postID INT,
	content TEXT,
	author CHAR(14)
)
BEGIN
	declare t date;
    select now() into t;
    INSERT INTO `Comment` (postID, created,content,author,likesCount)
    VALUES (postID, t, content, 
		author, 0);
    UPDATE Post
    SET Post.commentCount = commentCount + 1
    WHERE Post.postID = postID;
END//

CREATE PROCEDURE ownerAddUser(
    userID CHAR(14),
    membership ENUM('admin', 'user'),
    groupID int
)
BEGIN 
    INSERT INTO Member(userID, membership,groupID)
    VALUES (userID, membership, groupID);
END//

CREATE PROCEDURE ownerRemoveUser(
    userID CHAR(14),
    groupID INT
)
BEGIN
    DELETE 
    FROM Member
    WHERE Member.userID = userID AND Member.groupID = groupID;
END//

CREATE PROCEDURE ownerRemovePost(
    postID INT
)
BEGIN 
	declare i int;
	declare id int;
	select pageID into id from post P where P.postID = postID;  
    DELETE
    FROM Post
    WHERE Post.postID = postID;
    UPDATE `Page` P
    SET P.postCount = P.postCount-1
    where P.pageID = id;
END//

CREATE PROCEDURE ownerRemoveComment(
    commentID INT
)
BEGIN
	declare id int;
    select postID into id from `comment` C where C.commentID = commentID;
    DELETE
    FROM Comment
    WHERE Comment.commentID = commentID;
    update Post P
    set P.commentCount = P.commentCount-1
    where P.postID = id;
END//

CREATE PROCEDURE ownerEditPost(
    postID INT,
    content TEXT
)
BEGIN
    UPDATE Post
    SET Post.content = content
    WHERE Post.postID = postID;
END//

CREATE PROCEDURE ownerEditComment(
    commentID INT,
    content TEXT
)
BEGIN
    UPDATE `Comment` C
    SET C.content = content
    WHERE C.commentID = commentID;
END//

CREATE PROCEDURE ownerDeleteGroup(
    groupID INT
)
BEGIN
	
    DELETE
    FROM fGroup
    WHERE fGroup.groupID = groupID;
   
END//

CREATE PROCEDURE ownerRenameGroup(
    groupID INT,
    groupName VARCHAR(25)
)
BEGIN
   UPDATE fGroup
   SET fGroup.groupName = groupName
   WHERE fGroup.groupID = groupID;
END//

CREATE PROCEDURE joinGroup(
	userID CHAR(14),
    membership ENUM('admin', 'user'),
	groupID int
)
Begin
	declare t varchar(15);
    select G.Gstatus into t from fgroup G where G.groupID=groupID;
    if t = 'public'
    then
		call ownerAddUser(userID,'user',groupID);
	end if;
end//
    
create procedure unjoinGroup(
	userID Char(14),
    groupID int
)
Begin
	call ownerRemoveUser(userID,groupID);
end//

create procedure postOnGroup(
	userID char(14),
    groupId int,
	content TEXT
)
begin
	declare t datetime;
    declare pageID int;
    select now() into t;
    select P.pageID into pageID from page P where P.fGroup = groupID;
    if exists (select * from member M where M.groupID = groupId and M.userID = userID)
    then
    INSERT INTO Post (`owner`,pageID,postDate,content,commentCount,likesCount)
    VALUES (userID,  pageID,  t, 
		content, 0, 0);
    UPDATE `Page` 
    SET postCount = postCount + 1
    WHERE (`Page`.pageID = pageID);
    
    end if;
end//

create procedure commentOnGroup(
    postID INT,
	content TEXT,
	author CHAR(14)
)
begin
	declare pageID int;
    declare groupID int;
    select P.pageID into pageID from post P where P.postID = postID;
    select P.fgroup into groupID from Page P where P.pageID = pageID;
    if groupID is not null
    and exists(select* from member M where M.groupID = groupID and M.userID = author)
    then
		call ownerCommentPost(postID, content, author);
	end if;
end//

create procedure removeMyPost(
	postID int,
    userID char(14)
)
begin

	if (select P.owner from post P where postID=P.postID)=userID
    then
		call ownerRemovePost(postID);
	end if;
end//
	
create procedure removeMyComment(
	userID char(14),
    commentID int
)
begin
	if (select C.author from `comment` C where commentID=C.commentID)=userID
    then
		call ownerRemoveComment(commentID);
	end if;
end//

create procedure editMyPost(
	userID char(14),
    postID int,
    content text
)
begin
	if (select P.owner from post P where P.postID=postID)=userID
    then
		call ownerEditPost(postID,content);
	end if;
end//

create procedure editMyComment(
	userID char(14),
    commentID int,
    content text
)
begin
	if (select C.author from comment C where C.commentID = commentID)=userID
    then
		call ownerEditComment(commentID,content);
	end if;
end//	


CREATE PROCEDURE SendMessage (
	MSubject VARCHAR(100),
	MContent TEXT,
	MSenderId Char(14),
	MReceiverId char(14))
	BEGIN
    declare t datetime;
    select now() into t;
    INSERT INTO Message (MDate, MSubject, MContent, MSenderId, MReceiverId)
    VALUES ( t,MSubject, MContent, MSenderId, MReceiverId);
    END //

CREATE PROCEDURE DeleteMessage (
	MessageId INT)
	BEGIN
    DELETE FROM Message 
    WHERE (MessageId = Message.MessageId);
    END //

CREATE PROCEDURE LikePost (
    PostId INT,
    UserId char(14))
	BEGIN
    INSERT INTO LikePost (PostId, UserId)
    VALUES (PostId, UserId);
    UPDATE Post
    SET Post.likesCount = likesCount + 1
    WHERE Post.postID = PostId;
    END //
    
CREATE PROCEDURE LikeComment (
    CommentId INT,
    UserId char(14)) 
	BEGIN
    INSERT INTO LikeComment (CommentId, UserId)
    VALUES (CommentId, UserId);
    UPDATE `Comment`
    SET `Comment`.likesCount = likesCount + 1
    WHERE `Comment`.commentID = CommentId;
    END //

CREATE PROCEDURE UnlikePost (
    PostId INT,
    UserId char(14))
	BEGIN
    DELETE FROM LikePost
    WHERE (PostId = LikePost.PostId AND UserId = LikePost.UserId);
    UPDATE Post
    SET Post.likesCount = likesCount - 1
    WHERE Post.postID = PostId;
    END //
    
CREATE PROCEDURE UnlikeComment (
    CommentId INT,
    UserId char(14)) 
	BEGIN
    DELETE FROM LikeComment
    WHERE (CommentId = LikeComment.CommentId AND UserId = LikeComment.UserId);
    UPDATE `Comment`
    SET `Comment`.likesCount = likesCount - 1
    WHERE `Comment`.commentID = CommentId;
    END //
*/
###-----------------------MANAGER  TRANSACTIONS--------------####
DELIMITER //
#Add Employee
/*CREATE PROCEDURE AddEmployee(
	SSN INT,
    UserID CHAR(14),
    FirstName CHAR(50),
    LastName CHAR(50),
    Address CHAR(70),
    ZipCode INT,
    State CHAR(50),
    Telephone INT,
    HourlyRate DOUBLE,
    CName CHAR(50),
    passwd VARCHAR(100),
    city VARCHAR(15),
    email VARCHAR(50))
    BEGIN
    declare t datetime;
    select now() into t;
		INSERT INTO Employee(SSN,UserID,FirstName,LastName,StartDate,Address,ZipCode,State,Telephone,HourlyRate,CName) 
		VALUES(SSN,UserID,FirstName,LastName,t,Address,ZipCode,State,Telephone,HourlyRate,CName);
        call RegisterUser(UserID,passwd,LastName,FirstName,Address,city,State,email,0,'employee');
    END//



#Update Employee Info 
*/

#Remove Employee
/*CREATE PROCEDURE RemoveEmployee(
	SSN INT,
    UserID CHAR(14)
	)
    BEGIN
		DELETE FROM Employee  WHERE SSN=SSN;
	END//
*/
#Obtain Sales Report for a Month-query filter


    
#Produce listing of all items being advertised on the site-dislaying

#Produce a list of Transactions by ItemName or By UserName-displaying
#Produce a summary listing of revenue generated by particular item,item type,or Customer
#Determine which customer representative generated the most total revenue
#Determine which customer generated most total revenue
#Produce a list of most active items
#Produce a list of all customers who have purchased a particular item-filter
#Produce a list of all items being sold for a given company-filter
    
###-----------------------EMPLOYEE TRANSACTIONS--------------####
#Create an advertisement
/*CREATE PROCEDURE createAdvertisement(
	EmployeeID INT,
    MerchandiseType CHAR(50),
    CName CHAR(50),
    ItemName CHAR(70),
    UnitPrice DOUBLE,
    NoAvailableUnits INT
	)
    BEGIN
		declare t datetime;
		INSERT INTO Advertisements(EmployeeID,MerchandiseType,DatePublished,CName,ItemName,UnitPrice,NoAvailableUnits)
		VALUES(EmployeeID,MerchandiseType,t,CName,ItemName,UnitPrice,NoAvailableUnits);
	END //

#Delete an advertisement
CREATE PROCEDURE removeAdvertisement(
	AdvertisementID INT
	)
    BEGIN
		DELETE FROM Advertisements WHERE AdvertisementID=AdvertisementID;
    END//
	
#Record a transaction
CREATE PROCEDURE recordTransaction(
	AdvertisementID INT,
	NumberofUnits INT,
	AccountNumber INT,
	UserName CHAR(14)
	)
    BEGIN
		declare t datetime;
        INSERT INTO Sales(DatePurchase,AdvertisementID,NumberOfUnits,TotalPrice,AccountNumber,UserName)
        VALUES (t,AdvertisementID,NumberofUnits,0,AccountNumber,UserName);
UPDATE Sales S,
    AdvertisementRemoveEmployees A 
SET 
    S.TotalPrice = S.NumberofUnits * A.unitPrice
WHERE
    A.AdvertisementID = S.AdvertisementID;
    END//



#Add, Edit and DEmployeeelete information for a customer
#Produce customer mailing lists
 
#Produce a list of item suggestions for a given customer (based on that customer's past transactions)
#Retrieve a customer's current groups
#For each of a customer's accounts, the account history
#Best-Seller list of items
#Personalized item suggestion list
    
*/	
    
    

delimiter ;