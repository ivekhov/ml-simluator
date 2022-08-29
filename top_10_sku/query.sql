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
