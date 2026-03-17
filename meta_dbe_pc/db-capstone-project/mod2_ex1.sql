use LittleLemon;


-- Task 1
create view OrdersView as 
select OrderId, Quantity, TotalCost from Orders;

select * from OrdersView;

-- Task 2
select * from Menu limit 10;
select * from MenuCourses limit 10;


with ov as (
select * from OrdersView o_v where o_v.TotalCost >= 150
)
select 
	o.CustomerId,
    c.CustName,
	ov.OrderId, 
    ov.Totalcost,
    m.MenuName,
    mc.CourseName
from Orders o 
join ov on ov.OrderId = o.OrderId
join Customer c on o.CustomerId = c.CustomerId
join Menu m on o.MenuId = m.MenuId
join MenuCourses mc on m.CourseId = mc.CourseId
order by ov.TotalCost
;


-- Task 3

SELECT MenuName
FROM Menu
WHERE MenuId = ANY (
    SELECT MenuId 
    FROM Orders 
    WHERE Quantity > 2
);
