use LittleLemon;


-- Task 1

select *
from Bookings;

alter table Bookings
add column CustomerId int not null,
add constraint fk_bookings_customer
foreign key (CustomerId) references Customer(CustomerId)
on delete cascade
on update cascade;

select * from Customer;

set SQL_SAFE_UPDATES = 1;
update Bookings
set CustomerId = floor(1 + rand() * 50);


select * from Orders;

select * from Bookings
-- where Date = '2026-02-27 04:22:47';
where TableNo = 12;

-- Task 2
drop procedure if exists CheckBooking;
delimiter //
create procedure CheckBooking(in time_slot datetime, in table_no int)
begin
	declare table_status int default 0;
    
    select count(*) into table_status
    from Bookings
    where date = time_slot and TableNo = table_no;
    
    if table_status > 0 then
		select concat('table ', table_no, ' is already booked') as `Booking Status`;
	else
		select concat('table ', table_no, ' is available') as `Booking Status`; 
	end if;
end //
delimiter ;

call CheckBooking('2026-02-09 04:22:47', 12);


-- Task 3
drop procedure if exists AddValidBooking;
delimiter //
create procedure AddValidBooking(in time_slot datetime, in table_no int , in customer_id int)
begin
	declare current_booking int default 0;
    
    insert into Bookings(Date, TableNo, CustomerId)
    values (time_slot, table_no, customer_id);
    
    select count(*) into current_booking
    from Bookings where Date = time_slot and TableNo = table_no;
    
    if current_booking > 1 then
		commit;
        select concat('Table no ', table_no, ' is not available booking cancelled');
	else
		rollback;
        select concat('Table no', table_no, ' is available booking confirmed');
	end if;
end //
delimiter ;

call AddValidBooking('2026-02-09 03:00:00', 12, 1);




