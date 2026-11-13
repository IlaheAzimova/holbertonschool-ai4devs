# Data Model - EcoRide

## 1. Overview

EcoRide uses a relational database to store users, ride listings, bookings, and environmental impact estimates.

## 2. Entities

### Entity 1: User

Stores information about registered users.

| Field | Type | Constraints | Description |
|---|---|---|---|
| id | UUID | Primary Key | Unique user identifier |
| name | VARCHAR(100) | NOT NULL | User's name |
| email | VARCHAR(255) | UNIQUE, NOT NULL | User's email address |
| role | VARCHAR(20) | NOT NULL | Driver, passenger, or both |
| created_at | TIMESTAMP | NOT NULL | Account creation time |

### Entity 2: Ride

Stores ride listings created by drivers.

| Field | Type | Constraints | Description |
|---|---|---|---|
| id | UUID | Primary Key | Unique ride identifier |
| driver_id | UUID | Foreign Key → User.id | Ride owner |
| departure_location | VARCHAR(255) | NOT NULL | Starting location |
| destination | VARCHAR(255) | NOT NULL | Destination |
| departure_time | TIMESTAMP | NOT NULL | Departure date and time |
| total_seats | INTEGER | Positive | Total passenger seats |
| available_seats | INTEGER | NOT NULL | Remaining seats |
| price | DECIMAL(10,2) | NOT NULL | Price per passenger |
| status | VARCHAR(20) | NOT NULL | Scheduled, completed, or cancelled |
| created_at | TIMESTAMP | NOT NULL | Listing creation time |

**Business Rules**
- Available seats must be between zero and total seats.
- The departure time must be in the future when a ride is created.
- Only the ride owner can update the ride.
- Cancelled rides cannot accept new bookings.

### Entity 3: Booking

Stores passenger reservations.

| Field | Type | Constraints | Description |
|---|---|---|---|
| id | UUID | Primary Key | Unique booking identifier |
| ride_id | UUID | Foreign Key → Ride.id | Booked ride |
| passenger_id | UUID | Foreign Key → User.id | Passenger who booked |
| status | VARCHAR(20) | NOT NULL | Active or cancelled |
| booked_at | TIMESTAMP | NOT NULL | Booking creation time |

**Business Rules**
- A passenger cannot have multiple active bookings for the same ride.
- A booking can only be created if seats are available.
- Cancelling a booking restores one available seat.
- Booking and seat updates must be handled in a database transaction.

### Entity 4: EnvironmentalImpact

Stores estimated environmental savings from shared rides.

| Field | Type | Constraints | Description |
|---|---|---|---|
| id | UUID | Primary Key | Unique impact record |
| ride_id | UUID | Foreign Key → Ride.id | Associated ride |
| co2_saved_kg | DECIMAL(10,2) | NOT NULL | Estimated CO2 savings in kilograms |
| calculation_method | VARCHAR(100) | NOT NULL | Method used for calculation |
| calculated_at | TIMESTAMP | NOT NULL | Calculation timestamp |

The environmental impact value is an estimate based on assumptions about trip distance, vehicle emissions, and passenger numbers.

## 3. Entity Relationships

- One user can create many rides.
- One user can make many bookings.
- One ride can have many bookings.
- Each booking belongs to one passenger and one ride.
