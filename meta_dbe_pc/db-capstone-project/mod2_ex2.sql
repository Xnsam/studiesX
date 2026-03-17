use LittleLemon;

-- Task 1
drop procedure if exists GetMaxQuantity;
delimiter //
create procedure GetMaxQuantity(in input_order_id int)
begin
	if input_order_id is null then
		select max(Quantity) as MaxQty from Orders;
	else
		select max(Quantity) as MaxQty from Orders where OrderId = input_order_id;
	end if;
end //
delimiter ;

call GetMaxQuantity(null);


-- Task 2
prepare GetOrderDetail from 
"select OrderId, Quantity, TotalCost from Orders where CustomerId = ?";


set @id = 1;
execute GetOrderDetail using @id;

-- Task 3

select * from Orders limit 2;
prepare InsertValuesOrder from
"insert into Orders(OrderDate, Quantity, TotalCost, DeliveryId, StaffId, BookingId, MenuId, CustomerId)
values (?, ?, ?, ?, ?, ?, ?, ?)";

SET @OrderDate = '2026-03-09 13:30:00';
SET @Quantity = 5;
SET @TotalCost = 250.00;
SET @DeliveryId = 1;
SET @StaffId = 3;
SET @BookingId = 10;
SET @MenuId = 5;
SET @CustomerId = 1;

EXECUTE InsertValuesOrder USING 
    @OrderDate, 
    @Quantity, 
    @TotalCost, 
    @DeliveryId, 
    @StaffId, 
    @BookingId, 
    @MenuId, 
    @CustomerId;

DEALLOCATE PREPARE InsertValuesOrder;

select * from Orders where OrderId = 52;

drop procedure if exists CancelOrder;
delimiter //
create procedure CancelOrder(in input_order_id int)
begin
	delete from Orders where OrderId = input_order_id;
    
    select concat('Order ', input_order_id, ' is cancelled') as Confirmation;
end //
delimiter ;

call CancelOrder(52);


