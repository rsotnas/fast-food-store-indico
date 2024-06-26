CREATE TABLE fast_food_stores (
    StoreID INT PRIMARY KEY,
    StoreName VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL,
    Owner VARCHAR(100) NOT NULL,
    EstablishedYear INT NOT NULL,
    NumberOfEmployees INT NOT NULL
)

CREATE INDEX fast_food_stores_index ON fast_food_stores (StoreID)