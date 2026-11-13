# User Stories - EcoRide

## User Story 1: Create a Ride
**As a** driver,  
**I want** to create a ride listing with departure, destination, date, time, available seats, and price,  
**so that** passengers can find and join my journey.

**Acceptance Criteria**
- The driver must enter all required ride details.
- The system validates the date, price, and available seats.
- The ride appears in the list of available rides after successful creation.

**Priority:** MVP

## User Story 2: Search for Rides
**As a** passenger,  
**I want** to search for rides by departure location, destination, and date,  
**so that** I can find a suitable journey.

**Acceptance Criteria**
- Users can enter departure and destination locations.
- Users can filter rides by travel date.
- The system displays matching rides or a message when no results are found.

**Priority:** MVP

## User Story 3: View Ride Details
**As a** passenger,  
**I want** to view the details of a ride,  
**so that** I can decide whether to book it.

**Acceptance Criteria**
- The ride details include locations, date, time, price, and available seats.
- The system displays an appropriate message if the ride no longer exists.
- Only rides with available seats can be booked.

**Priority:** MVP

## User Story 4: Book a Ride
**As a** passenger,  
**I want** to reserve a seat on an available ride,  
**so that** I can travel with a driver going in the same direction.

**Acceptance Criteria**
- The passenger can book a ride with available seats.
- The system decreases the available seat count after a successful booking.
- The system prevents bookings when no seats remain.

**Priority:** MVP

## User Story 5: View My Bookings
**As a** passenger,  
**I want** to see my current ride bookings,  
**so that** I can keep track of my planned journeys.

**Acceptance Criteria**
- The system displays the passenger's bookings.
- Each booking includes the ride date, destination, price, and booking status.
- The passenger can distinguish active bookings from cancelled bookings.

**Priority:** MVP

## User Story 6: Cancel a Booking
**As a** passenger,  
**I want** to cancel a ride booking,  
**so that** I can free my reserved seat if my plans change.

**Acceptance Criteria**
- The passenger can cancel an active booking.
- The system updates the booking status to cancelled.
- The system restores one available seat for the ride.

**Priority:** MVP

## User Story 7: Manage My Rides
**As a** driver,  
**I want** to view and manage the rides I have created,  
**so that** I can keep my journey information up to date.

**Acceptance Criteria**
- The driver can view their own ride listings.
- The driver can update ride details.
- The driver cannot reduce the seat capacity below the number of existing bookings.

**Priority:** High

## User Story 8: View Environmental Impact
**As an** environmentally conscious user,  
**I want** to see an estimate of CO2 emissions saved through shared rides,  
**so that** I can understand the environmental benefit of ride-sharing.

**Acceptance Criteria**
- The system calculates estimated emissions savings using a documented simplified formula.
- The system displays the estimated savings in kilograms of CO2.
- The estimate is clearly identified as an approximation.

**Priority:** High

## User Story 9: Validate Ride Information
**As a** user,  
**I want** the system to validate ride and booking information,  
**so that** invalid data and booking errors are prevented.

**Acceptance Criteria**
- Required fields cannot be empty.
- Ride dates cannot be in the past.
- Prices and seat counts must be valid non-negative or positive values, as appropriate.

**Priority:** MVP

## User Story 10: Prevent Duplicate Bookings
**As a** passenger,  
**I want** to avoid booking the same ride more than once,  
**so that** I do not accidentally reserve multiple seats for myself.

**Acceptance Criteria**
- The system checks for an existing active booking by the same passenger.
- Duplicate active bookings are rejected.
- The passenger receives a clear message explaining the result.

**Priority:** MVP
