CREATE TABLE order_data (
  id int8 NOT NULL,
  order_date date NOT NULL,
  item varchar(255) NOT NULL,
  quantity int8 NOT NULL,
  price numeric NOT NULL,
  address varchar(255) NOT NULL
);
