use LittleLemon;


select * from Bookings limit 2;

-- Task 1
drop procedure if exists AddBooking;
delimiter //
create procedure AddBooking(in customer_id int, in time_slot datetime, in table_no int)
begin
	declare current_booking int default 0;
    declare booking_id int default 0;
    
    start transaction;
    
    insert into Bookings(Date, TableNo, CustomerId)
    values (time_slot, table_no, customer_id);
    
    select count(*) into current_booking
    from Bookings where Date = time_slot and TableNo = table_no and CustomerId = customer_id;
    
    if current_booking > 1 then
		rollback;
        select concat('Table No ', table_no, ' is already booked! Booking cancelled, try other slot');
	else
		commit;
        select BookingId into booking_id
        from Bookings where Date = time_slot and TableNo = table_no and CustomerId = customer_id;
        
        select concat('Table No ', table_no, ' is  booked! Booking confirmed Booking id ', booking_id);
	end if;
end //
delimiter ;

call AddBooking(2, '2026-03-10 02:00:00', 2);

-- Task 2
drop procedure if exists UpdateBooking;
delimiter //
create procedure UpdateBooking(in booking_id int, in booking_date datetime)
begin
	declare current_booking int default 0;
	start transaction;
    
    update Bookings
    set Date = booking_date 
    where BookingId = booking_id;
    
    select count(*) into current_booking
    from Bookings
    where BookingId = booking_id;
    
    if current_booking = 0 then
		rollback;
        select concat('Time slot ', booking_date, 'for booking id ', booking_id, ' is unavailble');
	else
		commit;
        select concat('Time slot ', booking_date, 'for booking id ', booking_id, ' is confirmed !');
	end if;
end //
delimiter ;

call UpdateBooking(61, '2026-03-10 02:00:00');

select * from Bookings
where BookingId = 61;

-- Task 3
drop procedure if exists CancelBooking;
delimiter //
create procedure CancelBooking(in booking_id int)
begin 
	declare current_booking int default 0;
    start transaction;
    delete from Bookings
    where BookingId = booking_id;
    
    select count(*) into current_booking
    from Bookings
    where BookingId = booking_id;
    
    if current_booking > 0 then
		rollback;
        select concat('booking id', booking_id, 'deletion failed');
	else
		commit;
        select concat('booking id', booking_id, 'deleted');
	end if;
end //
delimiter ;

call CancelBooking(61);