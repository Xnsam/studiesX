USE `LittleLemon`;

select column_name
from information_schema.columns
where table_name = 'Orders';

drop procedure if exists PopBaseTables;
DELIMITER //
create procedure PopBaseTables()
begin
	declare i int default 1;
    
    while i <= 50 do
		-- populate the addresses
		insert into Addresses(AddressId, City, Country, Pincode, State)
        values (i, concat('City', i),'CountryName', floor(1000 + rand() * 90000), 'StateName');
        
        -- populate menu components
        insert into MenuStarters(StarterId, StarterName)
        values (i, concat('Starter', i));
        
        insert into MenuCourses(CourseId, CourseName)
        values (i, concat('Course', i));
        
        insert into MenuDrinks(DrinkId, DrinkName)
        values (i, concat('Drinks', i));
        
        insert into MenuDesserts(DessertId, DessertName)
        values (i, concat('Desserts', i));
        
        insert into MenuCuisines(CuisineId, CuisineName)
        values (i, concat('Cuisine', i));
        
        -- populate staff
        insert into Staff (Name, PhoneNum, Email)
        values (concat('Staff_', i), floor(1000000 + rand() * 9000000), concat('staff', i, '@littlemon.com'));
        
        -- populate bookings
        insert into Bookings(Date, TableNo)
        values(now() - interval (rand() * 30) day, floor(1 * rand() * 20));
        
        set i = i + 1;
        
    end while;
    
	insert into OrderStatus (DeliveryStatus) 
	values ('Pending'), ('In progress'), ('Delivered'), ('Cancelled');
        
end //
DELIMITER ;
call PopBaseTables;



select * from MenuStarters;

drop procedure if exists PopL1;
delimiter //
create procedure PopL1()
begin
	declare i int default 1; 
    while i <= 50 do
		-- populate menu
        insert into Menu(CourseId, CuisineId, DessertId, DrinkId, StarterId)
        values (i, i, i, i, i);
        
        -- populate customers
        insert into Customer(AddressId, CustEmail, CustName, CustPhone)
        values (floor(1 + RAND() * 50), concat('Cust', i, '@customer',i, '.com'), concat('Customer_', i), floor(1000000 + RAND() * 90000000));
        
        set i = i + 1;
	end while;
end //
delimiter ;

call PopL1();

drop procedure if exists PopOrders;
delimiter //
create procedure PopOrders()
begin
	declare i int default 1;
    while i <= 50 do
		insert into Orders(OrderDate, Quantity, TotalCost, DeliveryId, StaffId, BookingId, MenuId, CustomerId)
        values (
			now() - interval (rand() * 10) day,
            floor(1 + rand() * 5),
            (rand() * 200),
            floor(1 + rand() * 4),
            floor(1 + rand() * 50),
            i,
            i,
            floor(1 + rand() * 50)
        );
        set i = i + 1;
    end while;
end // 
delimiter ;

call PopOrders();

SET FOREIGN_KEY_CHECKS = 1;


drop procedure if exists PopDeliveryStatus;
delimiter //
create procedure PopDeliveryStatus()
begin
	declare i int default 1;
    declare current_order_date datetime; 
    while i <= 50 do
		select OrderDate into current_order_date
        from Orders
        where OrderId = i;
        
        insert into OrderDeliveryStatus (OrderId, Status,  DeliveryTime)
        values (
			i,
            ELT(floor(1 + rand() * 4), 'Out for delivery', 'At Hub', 'Delivered', 'Delayed'),
            date_add(current_order_date, interval (30 + rand() * 60) minute)
        );
        set i = i + 1;
    end while;
end //
delimiter ; 

call PopDeliveryStatus();

select
	o.OrderId,
    c.CustName,
    ods.Status AS TrackingStatus,
    ods.DeliveryTime,
    m.MenuId,
    m.MenuName
from Orders o
join Customer c on o.CustomerId = c.CustomerId
join OrderDeliveryStatus ods on o.OrderId = ods.OrderId
join Menu m on o.MenuId = m.MenuId
limit 10;

select count(*) from Orders;
select count(*) from OrderDeliveryStatus;


alter table Menu
add column MenuName varchar(30);


select * from Menu;

set SQL_SAFE_UPDATES = 1;
update Menu m 
set MenuName = concat('MenuName', m.MenuId)
where MenuName is NULL;


