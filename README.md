# Almosand Crawler

## Goal
### 1- The AC should send a request to this endpoint https://dashboard.almosand.com/invoices/create with this data :
- customer id
- invoice date
- invoice items


### 2- The data will imported from multiply csv have :

The Invoices Csv:
- `invoicedate`
- `invoiceduedate`
- `id`

The Customers Csv:
- `id`

The Invoice_Items Csv:
- `tid`
- `product`
- `qty`
- `price`

So now I want to get the 
- `invoicedate (Invoices)`
- `invoiceduedate (Invoices)`
- `id (Customers)`

attach them to the request 

after that I want to take the `id (Invoices)` and get all items that match this id with `tid (Invoice_Items)`

like this query : ``` SELECT * FROM `Invoice_Items` WHERE `tid` = `id (Invoices)` ``` 

after I get the items in the invoice from the action above I want to attach the items to the request

`product`
`qty`
`price`

attach them to the request 

the invoice maybe has more than one item so I want to attach them all 

## Example

- after_disc	0
- alert[]	,
- code[]	
- counter	1
- cst	wal
- currency	0
- customer_id	2862
- discount_format	%
- discount_rate	0
- hsn[]	
- invoicedate	19-03-2024
- invoiceduedate	19-03-2024
- notes	
- order_id	
- p	
- product_description[]	,
- product_discount[]	,
- product_id[]	0,0
- product_name[]	test1,test2
- product_price[]	100,200
- product_qty[]	1.6,2.6
- product_subtotal[]	184.00,598.00
- product_tax[]	15,15
- refer	
- sales_channel	0
- serial[]	,
- ship_rate	0.00
- ship_tax	0.00
- ship_tax_type	none
- shipping	
- sub	
- subtotal	782.00
- tax_format	exclusive
- tax_format_static	exclusive
- tax_id	375
- term_id	47
- tid	2958
- total	782.00
- total_discount[]	0.00,0.00
- total_tax[]	24.00,78.00
- unit[]	,
- unit_m[]	1,1

those all the data we need to send to build an invoice

by the way the data I enter is :

- invoicedate	19-03-2024
- invoiceduedate	19-03-2024
- customer_id	2862
- the product array we use :
    - product_name[]	test1,test2
    - product_price[]	100,200
    - product_qty[]	1.6,2.6
    - product_subtotal[]	184.00,598.00
    - total_tax[]	24.00,78.00
    - tid	2958 (this is a just)