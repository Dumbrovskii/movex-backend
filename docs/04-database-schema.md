# Database Schema

**Document ID:** DBS-001  
**Product:** MoveX  
**Version:** 1.0  
**Status:** Draft

---
# Users

## Description

Stores all platform users.

A user may request rides as a passenger.
A user may also become a driver through the `drivers` table.

| Column     | Type         | Constraints      | Description                  |
| ---------- | ------------ | ---------------- | ---------------------------- |
| id         | BIGINT       | PK               | Unique user identifier.      |
| phone      | VARCHAR(30)  | UNIQUE, NOT NULL | User phone number.           |
| full_name  | VARCHAR(100) | NOT NULL         | User full name.              |
| email      | VARCHAR(254) | UNIQUE, NULL     | User email address.          |
| created_at | TIMESTAMPTZ  | NOT NULL         | Record creation timestamp.   |
| updated_at | TIMESTAMPTZ  | NOT NULL         | Last modification timestamp. |
| deleted_at | TIMESTAMPTZ  | NULL             | Soft deletion timestamp.     |

---
# Drivers

## Description

Represents users authorized to provide transportation services.

A driver cannot exist without an associated user.

| Column     | Type         | Constraints       | Description                  |
| ---------- | ------------ | ----------------- | ---------------------------- |
| user_id    | BIGINT       | PK, FK → users.id | Associated user.             |
| status     | DriverStatus | NOT NULL          | Current driver status.       |
| created_at | TIMESTAMPTZ  | NOT NULL          | Record creation timestamp.   |
| updated_at | TIMESTAMPTZ  | NOT NULL          | Last modification timestamp. |
| deleted_at | TIMESTAMPTZ  | NULL              | Soft deletion timestamp.     |

### DriverStatus

| Value     | Description                                          |
| --------- | ---------------------------------------------------- |
| Pending   | Waiting for verification.                            |
| Verified  | Allowed to accept ride requests.                     |
| Suspended | Temporarily prohibited from accepting ride requests. |

---
# Rides

## Description

Represents a transportation request created by a passenger and fulfilled by a driver.

| Column              | Type                   | Constraints                | Description                           |
| ------------------- | ---------------------- | -------------------------- | ------------------------------------- |
| id                  | BIGINT                 | PK                         | Unique ride identifier.               |
| passenger_id        | BIGINT                 | FK → users.id, NOT NULL    | User who requested the ride.          |
| assigned_driver_id  | BIGINT                 | FK → drivers.user_id, NULL | Assigned driver. NULL until accepted. |
| pickup_address      | TEXT                   | NOT NULL                   | Pickup address.                       |
| pickup_geo          | GEOGRAPHY(Point, 4326) | NOT NULL                   | Pickup coordinates.                   |
| destination_address | TEXT                   | NOT NULL                   | Destination address.                  |
| destination_geo     | GEOGRAPHY(Point, 4326) | NOT NULL                   | Destination coordinates.              |
| status              | RideStatus             | NOT NULL                   | Current ride status.                  |
| created_at          | TIMESTAMPTZ            | NOT NULL                   | Record creation timestamp.            |
| updated_at          | TIMESTAMPTZ            | NOT NULL                   | Last modification timestamp.          |

### RideStatus

| Value | Description |
|------------|-----------------------------------------------------------|
| Requested | Ride has been created and is waiting for a driver. |
| Accepted | A driver has accepted the ride request. |
| InProgress | The ride is currently in progress. |
| Completed | The ride has been successfully completed. |
| Cancelled | The ride has been cancelled before completion. |

---
# Payments

## Description

Represents payment information associated with a ride.

Each ride may have at most one payment.

| Column         | Type          | Constraints                     | Description                                       |
| -------------- | ------------- | ------------------------------- | ------------------------------------------------- |
| id             | BIGINT        | PK                              | Unique payment identifier.                        |
| ride_id        | BIGINT        | FK → rides.id, UNIQUE, NOT NULL | Associated ride.                                  |
| amount         | NUMERIC(10,2) | NOT NULL                        | Payment amount.                                   |
| currency       | CHAR(3)       | NOT NULL                        | ISO 4217 currency code.                           |
| status         | PaymentStatus | NOT NULL                        | Current payment status.                           |
| transaction_id | TEXT          | UNIQUE, NULL                    | External payment provider transaction identifier. |
| created_at     | TIMESTAMPTZ   | NOT NULL                        | Record creation timestamp.                        |
| updated_at     | TIMESTAMPTZ   | NOT NULL                        | Last modification timestamp.                      |
### PaymentStatus

| Value | Description |
|------------|-----------------------------------------------|
| Pending | Payment has been created but not completed. |
| Authorized | Funds have been authorized. |
| Paid | Payment has been successfully completed. |
| Failed | Payment failed. |
| Refunded | Payment has been refunded. |

---
# Ratings

## Description

Represents a rating submitted after a completed ride.

A ride may have multiple ratings.

| Column       | Type        | Constraints             | Description                    |
| ------------ | ----------- | ----------------------- | ------------------------------ |
| id           | BIGINT      | PK                      | Unique rating identifier.      |
| ride_id      | BIGINT      | FK → rides.id, NOT NULL | Associated ride.               |
| author_id    | BIGINT      | FK → users.id, NOT NULL | User who submitted the rating. |
| recipient_id | BIGINT      | FK → users.id, NOT NULL | User being rated.              |
| score        | SMALLINT    | NOT NULL                | Rating score (1–5).            |
| comment      | TEXT        | NULL                    | Optional review comment.       |
| created_at   | TIMESTAMPTZ | NOT NULL                | Record creation timestamp.     |
| updated_at   | TIMESTAMPTZ | NOT NULL                | Last modification timestamp.   |
### Constraints

| Constraint | Description |
|------------|------------------------------------------------------------|
| CHECK (score BETWEEN 1 AND 5) | Rating score must be between 1 and 5. |
| CHECK (author_id <> recipient_id) | A user cannot rate themselves. |

---
# Notifications

## Description

Represents notifications delivered to users.

Notifications are informational records and may be permanently deleted after they are no longer needed.

| Column     | Type             | Constraints             | Description                               |
| ---------- | ---------------- | ----------------------- | ----------------------------------------- |
| id         | BIGINT           | PK                      | Unique notification identifier.           |
| user_id    | BIGINT           | FK → users.id, NOT NULL | Notification recipient.                   |
| type       | NotificationType | NOT NULL                | Notification category.                    |
| title      | TEXT             | NOT NULL                | Notification title.                       |
| message    | TEXT             | NOT NULL                | Notification content.                     |
| created_at | TIMESTAMPTZ      | NOT NULL                | Record creation timestamp.                |
| read_at    | TIMESTAMPTZ      | NULL                    | Timestamp when the notification was read. |
### NotificationType

| Value | Description |
|------------|-----------------------------------------------|
| RideRequested | A new ride request has been created. |
| RideAccepted | A driver accepted the ride request. |
| RideStarted | The ride has started. |
| RideCompleted | The ride has been completed. |
| RideCancelled | The ride has been cancelled. |
| PaymentSucceeded | Payment completed successfully. |
| PaymentFailed | Payment failed. |
