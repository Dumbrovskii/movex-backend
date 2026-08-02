# Domain Model

**Document ID:** DOM-001  
**Product:** MoveX  
**Version:** 1.0  
**Status:** Draft

---
# Purpose

This document defines the core business domain of the MoveX platform.

It establishes the common business vocabulary used throughout the product and describes the primary business entities and the relationships between them.

This document intentionally excludes implementation details such as database design, APIs, and software architecture.

---
# Core Domain

The MoveX domain is centered around facilitating transportation between passengers and drivers.

A passenger requests transportation.

A driver accepts and performs transportation.

The platform coordinates the interaction between both parties.

---
# Domain Entities

## Passenger

A person requesting transportation services.

A passenger may request multiple rides over time.

---
## Driver

A person authorized to provide transportation services.

A driver progresses through a verification lifecycle before becoming eligible to accept ride requests.

A driver may complete many rides over time.

---
## Ride

A transportation service requested by a passenger and fulfilled by a driver.

A ride progresses through a defined lifecycle from creation to completion or cancellation.

---
## Payment

A financial transaction associated with a completed ride.

---
## Rating

Feedback provided by one participant to another after a completed ride.

---
## Notification

A message delivered by the platform to inform users about important events.

---
# Relationships

| Entity    | Relationship | Entity       |
| --------- | ------------ | ------------ |
| Passenger | requests     | Ride         |
| Driver    | fulfills     | Ride         |
| Ride      | produces     | Payment      |
| Ride      | generates    | Rating       |
| Platform  | sends        | Notification |

---
# Ride Lifecycle

A ride may exist in one of the following business states:
- Requested
- Accepted
- Driver Arriving
- In Progress
- Completed
- Cancelled

---
# Business Rules

The following business rules apply to the domain.
- A ride has exactly one passenger.
- A ride has at most one driver.
- A driver may participate in only one active ride at a time.
- Only verified drivers may accept ride requests.
- A passenger may have only one active ride at a time.
- A completed ride cannot be modified.
- A payment may exist only for a completed ride.
- Ratings may be submitted only after ride completion.

---
# Domain Glossary

| Term                     | Definition                                                                   |
| ------------------------ | ---------------------------------------------------------------------------- |
| Passenger                | A person requesting transportation services.                                 |
| Driver                   | A person authorized to provide transportation services.                      |
| Driver Status            | The current verification state of a driver.                                  |
| Driver Status: Pending   | The driver is awaiting verification.                                         |
| Driver Status: Verified  | The driver is eligible to accept ride requests.                              |
| Driver Status: Suspended | The driver is temporarily prohibited from accepting ride requests.           |
| Ride                     | A transportation service requested by a passenger and fulfilled by a driver. |
| Payment                  | A financial transaction associated with a completed ride.                    |
| Rating                   | Feedback submitted after a completed ride.                                   |
| Notification             | A platform message informing users about important events.                   |
| Ride: Requested          | A ride has been created and is waiting for a driver.                         |
| Ride: Accepted           | A driver has accepted the ride request.                                      |
| Ride: Driver Arriving    | The driver is traveling to the pickup location.                              |
| Ride: In Progress        | The passenger is being transported.                                          |
| Ride: Completed          | The ride has finished successfully.                                          |
| Ride: Cancelled          | The ride was terminated before completion.                                   |
| Active Ride              | A ride in Requested, Accepted, Driver Arriving, or In Progress state.        |

---
# Domain Boundaries

The initial domain includes:
- User management
- Driver management
- Ride management
- Payments
- Ratings
- Notifications

The following domains are currently excluded:
- Food delivery
- Parcel delivery
- Fleet management
- Advertising
- Loyalty programs