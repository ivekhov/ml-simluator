-- Вам дан доступ к таблице sku_dict_another_one. 
-- Напишите запрос и постройте дашборд в Redash 
-- с демонстрацией TOP10 SKU, которые имеют больше всего вендоров, которые их продают.

-- Также назовите столбцы sku_type и vendors, 
-- обратите внимание, что столбцы должны быть 
-- именно в таком порядке. Вам нужно будет 
-- выгрузить ваше решение в формате csv и отправить его в форму ниже.

select 
    sku_type as sku_type
    , count(distinct vendor) as vendors
from sku_dict_another_one
group by sku_type
order by count(distinct vendor) desc
limit 10;

select *
from sku_dict_another_one;

--
select 
    brand as brand
    -- , count(distinct sku_type) as count_sku
    , count( sku_type) as count_sku
from sku_dict_another_one
-- where brand is not null 
group by brand
order by count(sku_type) desc 
limit 10;

--

select 
    brand as brand 
    , count(distinct sku_type) as count_sku
    -- , count( sku_type) as count_sku
from sku_dict_another_one
-- where brand is not null 
group by brand
order by count(distinct sku_type) desc 

limit 10;
--

select 
    brand as brand 
    , count(distinct sku_type) as count_sku
    -- , count( sku_type) as count_sku
from sku_dict_another_one
-- where brand is not null 
group by brand
order by count(distinct sku_type) desc 

limit 10;

--

select 
    vendor as vendor 
    , count( sku_type) as sku
from sku_dict_another_one
group by vendor
order by count( sku_type) desc 

limit 10;




