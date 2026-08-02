# Database Design

**Document ID:** DBD-001  
**Product:** MoveX  
**Version:** 1.0  
**Status:** Draft

---
# Purpose

This document defines the logical database design for the MoveX platform.

It identifies the persistent data structures required to support the business domain and establishes the relationships between them.

Implementation details such as SQL migrations, indexes, storage optimization, and database-specific features are intentionally excluded from this document.

---
# Design Principles

The database design follows these principles:

- Every business entity has a unique identifier.
- Data redundancy should be minimized.
- Referential integrity must be enforced.
- Historical business data should be preserved.
- Business constraints should be enforced whenever possible.
- The schema should support future evolution without breaking existing data.

---
# Logical Data Model

## User

Represents a registered platform user.

A user may act as a passenger, a driver, or both.

### Attributes

- Id
- Phone Number
- Full Name
- Email
- Status
- Created At
- Updated At
- Deleted At

---
## Driver

Represents a user authorized to provide transportation services.

### Attributes

- Id
- User Id
- Driver Status
- Created At
- Updated At
- Deleted At

---
## Ride

Represents a transportation request.

### Attributes

- Id
- Passenger Id
- Driver Id
- Pickup Location
- Destination Location
- Status
- Requested At
- Accepted At
- Started At
- Completed At
- Cancelled At

---
## Payment

Represents payment for a completed ride.

### Attributes

- Id
- Ride Id
- Amount
- Currency
- Status
- Paid At

---
## Rating

Represents feedback submitted after a completed ride.

### Attributes

- Id
- Ride Id
- Author Id
- Recipient Id
- Score
- Comment
- Created At

---
## Notification

Represents a notification delivered to a user.

### Attributes

- Id
- User Id
- Type
- Title
- Body
- Read At
- Created At

---
# Relationships

| Parent | Child | Cardinality |
|---------|-------|-------------|
| User | Driver | 1 : 0..1 |
| User | Ride (Passenger) | 1 : N |
| Driver | Ride | 1 : N |
| Ride | Payment | 1 : 0..1 |
| Ride | Rating | 1 : N |
| User | Notification | 1 : N |

---
# Business Constraints

- Every ride must have exactly one passenger.
- A ride may have one assigned driver.
- A payment cannot exist without a ride.
- Ratings are allowed only after ride completion.
- A notification always belongs to exactly one user.

---
# Audit Requirements

The following entities shall maintain audit information:

- User
- Driver
- Ride
- Payment
- Rating
- Notification

Each record should support:

- Created At
- Updated At

Where applicable:

- Deleted At (soft deletion)

---
# Future Extensions

The schema is expected to support future entities including:

- Vehicle
- Driver Documents
- Ride Offers
- Promotions
- Wallet
- Driver Earnings
- Fleet
- Trip Tracking