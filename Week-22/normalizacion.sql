======================================================================

                        Normalización #1

======================================================================

Order ID	Customer Name	Customer Phone	Address	        ItemID	  Item Name	        Price	Quantity	Special Request	    Delivery Time
001	        Alice	        123-456-7890	123 Main St	    101	       Cheeseburger	    $8	    2	        No onions	        6:00 PM
001	        Alice	        123-456-7890	123 Main St	    102	        Fries	        $3	    1	        Extra ketchup	    6:00 PM
002	        Bob	            987-654-3210	456 Elm St	    103	        Pizza	        $12	    1	        Extra cheese	    7:30 PM
002	        Bob	            987-654-3210	4th Avenue	    102	        Fries	        $3	    2	        None	            7:30 PM
003	        Claire	        555-123-4567	789 Oak St	    105	        Salad	        $6	    1	        No croutons	        12:00 PM
004	        Claire	        555-123-4567	464 Georgia St	106	        Water	        $1	    1	        None	            5:00 PM

1FN: Se define PK compuesta (Order_ID, Item_ID)
2FN: Se separan Orders, Items y Order_Items eliminando dependencias parciales
3FN: Se separan Customers y Addresses eliminando dependencias transitivas

-- ======================================================================
--                    1FN: PK compuesta (Order_ID, Item_ID)
-- ======================================================================
-- Order_ID (PK) | Item_ID (PK) | Customer_Name | Phone        | Address      | Item_Name    | Price | Qty | Special_Request | Delivery_Time
-- 001           | 101          | Alice         | 123-456-7890 | 123 Main St  | Cheeseburger | $8    | 2   | No onions       | 6:00 PM
-- 001           | 102          | Alice         | 123-456-7890 | 123 Main St  | Fries        | $3    | 1   | Extra ketchup   | 6:00 PM
-- 002           | 103          | Bob           | 987-654-3210 | 456 Elm St   | Pizza        | $12   | 1   | Extra cheese    | 7:30 PM

-- ======================================================================
--              2FN: Se separan Orders, Items y Order_Items
-- ======================================================================

-- Orders
-- Order_ID (PK) | Customer_Name | Phone        | Address        | Delivery_Time
-- 001           | Alice         | 123-456-7890 | 123 Main St    | 6:00 PM
-- 002           | Bob           | 987-654-3210 | 456 Elm St     | 7:30 PM

-- Items
-- Item_ID (PK) | Item_Name    | Price
-- 101          | Cheeseburger | $8
-- 102          | Fries        | $3

-- Order_Items
-- Order_ID (FK) | Item_ID (FK) | Quantity | Special_Request
-- 001           | 101          | 2        | No onions
-- 001           | 102          | 1        | Extra ketchup

-- ======================================================================
--         3FN: Se separan Customers y Addresses de Orders
-- ======================================================================

-- Customers
-- id (PK) | Customer_Name | Phone
-- 1       | Alice         | 123-456-7890

-- Addresses
-- id (PK) | Address
-- 1       | 123 Main St

Para poder solucionar el ejercicio tuve que hacerlo en Draw sql
https://drawsql.app/draw?t=e373592c-3533-47eb-9575-929322392698&view=1




======================================================================

                        Normalización #2

======================================================================


VIN	Make	    Model	        Year	Color	OwnerID	    Owner Name	Owner Phone	    Insurance Company	Insurance Policy
1HGCM82633A	    Honda Accord	2003	Silver	101	        Alice	    123-456-7890	ABC Insurance	    Fire & Theft
1HGCM82633A	    Honda Accord	2003	Silver	102	        Bob	        987-654-3210	XYZ Insurance	    Full Cover
5J6RM4H79EL	    Honda CR-V	    2014	Blue	103	        Claire	    555-123-4567	DEF Insurance	    Collision
1G1RA6EH1FU	    Chevrolet Volt	2015	Red	    104	        Dave	    111-222-3333	GHI Insurance	    Basic Legal


1FN: Se define PK compuesta (VIN, Owner_ID)
2FN: Se separan Cars, Owners y Owner_cars eliminando dependencias parciales
3FN: Se separan makers, models, insurance_companies e insurance_policies eliminando dependencias transitivas


-- ======================================================================
--                    1FN: PK compuesta (VIN, Owner_ID)
-- ======================================================================
-- VIN (PK)     | Owner_ID (PK) | Make      | Model  | Year | Color  | Owner_Name | Owner_Phone  | Insurance_Company | Insurance_Policy
-- 1HGCM82633A  | 101           | Honda     | Accord | 2003 | Silver | Alice      | 123-456-7890 | ABC Insurance     | Fire & Theft
-- 1HGCM82633A  | 102           | Honda     | Accord | 2003 | Silver | Bob        | 987-654-3210 | XYZ Insurance     | Full Cover
-- 5J6RM4H79EL  | 103           | Honda     | CR-V   | 2014 | Blue   | Claire     | 555-123-4567 | DEF Insurance     | Collision
-- 1G1RA6EH1FU  | 104           | Chevrolet | Volt   | 2015 | Red    | Dave       | 111-222-3333 | GHI Insurance     | Basic Legal

-- ======================================================================
--              2FN: Se separan Cars, Owners y Owner_cars
-- ======================================================================

-- Cars
-- VIN (PK)     | Make      | Model  | Year | Color
-- 1HGCM82633A  | Honda     | Accord | 2003 | Silver
-- 5J6RM4H79EL  | Honda     | CR-V   | 2014 | Blue
-- 1G1RA6EH1FU  | Chevrolet | Volt   | 2015 | Red

-- Owners
-- Owner_ID (PK) | Owner_Name | Owner_Phone
-- 101           | Alice      | 123-456-7890
-- 102           | Bob        | 987-654-3210
-- 103           | Claire     | 555-123-4567
-- 104           | Dave       | 111-222-3333

-- Owner_cars
-- VIN (FK)     | Owner_ID (FK) | Insurance_Company | Insurance_Policy
-- 1HGCM82633A  | 101           | ABC Insurance     | Fire & Theft
-- 1HGCM82633A  | 102           | XYZ Insurance     | Full Cover
-- 5J6RM4H79EL  | 103           | DEF Insurance     | Collision
-- 1G1RA6EH1FU  | 104           | GHI Insurance     | Basic Legal

-- ======================================================================
--         3FN: Se separan makers, models, insurance_companies e insurance_policies
-- ======================================================================

-- makers
-- id | maker_name
-- 1  | Honda
-- 2  | Chevrolet

-- models
-- id | model_name | maker_id
-- 1  | Accord     | 1
-- 2  | CR-V       | 1
-- 3  | Volt       | 2

-- insurance_companies
-- id | company_name
-- 1  | ABC Insurance
-- 2  | XYZ Insurance
-- 3  | DEF Insurance
-- 4  | GHI Insurance

-- insurance_policies
-- id | policy_name  | company_id
-- 1  | Fire & Theft | 1
-- 2  | Full Cover   | 2
-- 3  | Collision    | 3
-- 4  | Basic Legal  | 4


Para hacer este tambien tuve que hacerlo en DRAW
https://drawsql.app/teams/shalston/diagrams/normalizacion-2



