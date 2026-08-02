# Use Cases

**Document ID:** UC-001  
**Product:** MoveX  
**Version:** 1.0  
**Status:** Draft

---
# Authentication

## UC-01-01 Request Verification Code

### Goal

Request a one-time verification code for phone number authentication.

### Primary Actor

Guest

### Preconditions

- The user provides a valid phone number.

### Trigger

The user initiates the sign-in process.

### Main Flow

1. The user enters a phone number.
2. The system validates the phone number format.
3. The system generates a one-time verification code.
4. The system stores the verification code with an expiration time.
5. The system sends the verification code via SMS.
6. The system confirms that the verification code has been sent.

### Alternative Flows

**A1. Invalid phone number**

- The system rejects the request.
- The user is asked to provide a valid phone number.

**A2. SMS delivery failed**

- The system reports that the verification code could not be sent.

**A3. Too many requests**

- The system rejects the request due to rate limiting.

### Postconditions

- A valid verification code exists for the provided phone number.
- The verification code has an expiration time.

---
## UC-01-02 Verify Verification Code

### Goal

Verify the one-time verification code and authenticate the user.

If the user does not exist, a new user account is created automatically.

### Primary Actor

Guest

### Preconditions

- A valid verification code has been issued for the provided phone number.
- The verification code has not expired.

### Trigger

The user submits the verification code received via SMS.

### Main Flow

1. The user enters the phone number and verification code.
2. The system validates the verification code.
3. The system checks whether the verification code has expired.
4. The system searches for an existing user with the provided phone number.
5. If no user exists, the system creates a new user account.
6. The system permanently invalidates the verification code.
7. The system issues an access token.
8. The system issues a refresh token.
9. The system stores the refresh token in Redis with an expiration time.
10. The system authenticates the user.

### Alternative Flows

**A1. Invalid verification code**

- The system rejects the verification request.
- The user is informed that the verification code is invalid.

**A2. Verification code expired**

- The system rejects the verification request.
- The user is asked to request a new verification code.

**A3. Verification code already used**

- The system rejects the verification request.

### Postconditions

- The user is authenticated.
- A user account exists for the verified phone number.
- The verification code is invalidated.
- A valid access token has been issued.
- A valid refresh token has been issued and stored in Redis.

---
## UC-01-03 Refresh Access Token

### Goal

Obtain a new access token using a valid refresh token.

### Primary Actor

Authenticated User

### Preconditions

- The user possesses a refresh token that exists in Redis and has not expired.

### Trigger

The access token has expired.

### Main Flow

1. The user submits a refresh token.
2. The system validates the refresh token.
3. The system verifies that the refresh token exists in Redis.
4. The system issues a new access token.
5. The system returns the new access token.

### Alternative Flows

**A1. Invalid or expired refresh token**

- The system rejects the request.

**A2. Expired refresh token**

- The system rejects the request.
- The user must authenticate again.

### Postconditions

- A new access token has been issued.

---
## UC-01-04 Logout

### Goal

Terminate the current authenticated session.

### Primary Actor

Authenticated User

### Preconditions

- The user is authenticated.

### Trigger

The user requests to log out.

### Main Flow

1. The user requests to log out.
2. The system removes the refresh token from Redis.
3. The system confirms that the user has been logged out.

### Alternative Flows

None.

### Postconditions

- The refresh token is no longer valid.
- The user must authenticate again to obtain new tokens.

---
# Users

## UC-02-01 Get Current User

### Goal

Retrieve the authenticated user's profile.

### Primary Actor

Authenticated User

### Preconditions

- The user is authenticated.

### Trigger

The user requests their profile information.

### Main Flow

1. The user requests their profile.
2. The system validates the access token.
3. The system retrieves the user's profile.
4. The system returns the profile information.

### Alternative Flows

**A1. Invalid access token**

- The system rejects the request.

**A2. User not found**

- The system returns an error.

### Postconditions

- The user's profile information has been returned.

---
## UC-02-02 Update User Profile

### Goal

Update the authenticated user's full name and email address.

### Primary Actor

Authenticated User

### Preconditions

- The user is authenticated.

### Trigger

The user submits updated profile information.

### Main Flow

1. The user submits a full name and/or email address.
2. The system validates the submitted data.
3. The system updates the user's profile.
4. The system returns the updated profile.

### Alternative Flows

**A1. Invalid access token**

- The system rejects the request.

**A2. Invalid profile data**

- The system rejects the request and returns validation errors.

### Postconditions

- The user's profile has been updated.

---
# Drivers

## UC-03-01 Become Driver

### Goal

Create a driver profile for an authenticated user.

### Primary Actor

Authenticated User

### Preconditions

- The user is authenticated.
- The user does not already have a driver profile.

### Trigger

The user requests to become a driver.

### Main Flow

1. The user submits the required driver information.
2. The system validates the submitted data.
3. The system creates a driver profile.
4. The system sets the driver status to `Pending`.
5. The system returns the created driver profile.

### Alternative Flows

**A1. Driver profile already exists**

- The system rejects the request.

**A2. Invalid driver information**

- The system rejects the request and returns validation errors.

### Postconditions

- A driver profile exists for the user.
- The driver's status is `Pending`.

---
## UC-03-02 Update Driver Status

### Goal

Update the driver's status.

### Primary Actor

System Administrator

### Preconditions

- The driver profile exists.

### Trigger

An administrator reviews the driver.

### Main Flow

1. The administrator selects a driver.
2. The administrator assigns a new driver status.
3. The system validates the status transition.
4. The system updates the driver's status.
5. The system returns the updated driver profile.

### Alternative Flows

**A1. Driver not found**

- The system returns an error.

**A2. Invalid status transition**

- The system rejects the request.

### Postconditions

- The driver's status has been updated.

---
# Rides

## UC-04-01 Request Ride

### Goal

Create a new ride request.

### Primary Actor

Authenticated User

### Preconditions

- The user is authenticated.
- No active ride exists for the user.

### Trigger

The user submits a ride request.

### Main Flow

1. The user submits the pickup and destination locations.
2. The system validates the submitted data.
3. The system creates a new ride.
4. The system sets the ride status to `Requested`.
5. The system returns the created ride.

### Alternative Flows

**A1. Invalid ride data**

- The system rejects the request and returns validation errors.

**A2. Active ride already exists**

- The system rejects the request.

### Postconditions

- A new ride exists.
- The ride status is `Requested`.

---
## UC-04-02 Accept Ride

### Goal

Assign a driver to a ride.

### Primary Actor

Driver

### Preconditions

- The driver is authenticated.
- The driver status is `Verified`.
- The ride status is `Requested`.

### Trigger

The driver accepts a ride.

### Main Flow

1. The driver selects a requested ride.
2. The system verifies that the ride is still available.
3. The system assigns the driver to the ride.
4. The system sets the ride status to `Accepted`.
5. The system returns the updated ride.

### Alternative Flows

**A1. Ride already accepted**

- The system rejects the request.

**A2. Driver is not verified**

- The system rejects the request.

### Postconditions

- The ride has an assigned driver.
- The ride status is `Accepted`.

---
## UC-04-03 Cancel Ride

### Goal

Cancel an existing ride.

### Primary Actor

Passenger or Driver

### Preconditions

- The user is authenticated.
- The ride exists.
- The ride status is `Requested` or `Accepted`.

### Trigger

The passenger or driver requests to cancel the ride.

### Main Flow

1. The passenger or driver requests to cancel the ride.
2. The system verifies that the ride status is `Requested` or `Accepted`.
3. The system updates the ride status to `Cancelled`.
4. The system returns the updated ride.

### Alternative Flows

**A1. Ride not found**

- The system returns an error.

**A2. Ride cannot be cancelled**

- - The system rejects the request because the ride is already `InProgress`, `Completed`, or `Cancelled`.

### Postconditions

- The ride status is `Cancelled`.

---
## UC-04-04 Start Ride

### Goal

Start an accepted ride.

### Primary Actor

Driver

### Preconditions

- The driver is authenticated.
- The ride exists.
- The ride status is `Accepted`.

### Trigger

The driver starts the ride.

### Main Flow

1. The driver requests to start the ride.
2. The system verifies that the ride status is `Accepted`.
3. The system updates the ride status to `InProgress`.
4. The system returns the updated ride.

### Alternative Flows

**A1. Invalid ride status**

- The system rejects the request.

### Postconditions

- The ride status is `InProgress`.

---
## UC-04-05 Complete Ride

### Goal

Complete an active ride.

### Primary Actor

Driver

### Preconditions

- The driver is authenticated.
- The ride exists.
- The ride status is `InProgress`.

### Trigger

The driver completes the ride.

### Main Flow

1. The driver requests to complete the ride.
2. The system verifies that the ride status is `InProgress`.
3. The system updates the ride status to `Completed`.
4. The system returns the updated ride.

### Alternative Flows

**A1. Invalid ride status**

- The system rejects the request.

### Postconditions

- The ride status is `Completed`.

---
# Payments

## UC-05-01 Create Payment

### Goal

Create a payment for a completed ride.

### Primary Actor

Passenger

### Preconditions

- The passenger is authenticated.
- The ride exists.
- The ride status is `Completed`.
- No payment exists for the ride.

### Trigger

The passenger initiates the payment process.

### Main Flow

1. The passenger requests to pay for the ride.
2. The system verifies that the ride status is `Completed`.
3. The system verifies that no payment already exists.
4. The system creates a payment.
5. The system sets the payment status to `Pending`.
6. The system returns the payment information.

### Alternative Flows

**A1. Ride not found**

- The system returns an error.

**A2. Ride is not completed**

- The system rejects the request.

**A3. Payment already exists**

- The system rejects the request.

### Postconditions

- A payment exists for the ride.
- The payment status is `Pending`.

---
# Ratings

## UC-06-01 Submit Rating

### Goal

Submit a rating after a completed ride.

### Primary Actor

Passenger or Driver

### Preconditions

- The user is authenticated.
- The ride exists.
- The ride status is `Completed`.
- The user participated in the ride.
- The user has not already submitted a rating for the ride.

### Trigger

The user submits a rating.

### Main Flow

1. The user submits a rating and an optional comment.
2. The system validates the submitted data.
3. The system verifies that the user participated in the ride.
4. The system verifies that no previous rating exists from the user for the ride.
5. The system creates the rating.
6. The system returns the created rating.

### Alternative Flows

**A1. Ride not found**

- The system returns an error.

**A2. Ride is not completed**

- The system rejects the request.

**A3. Rating already exists**

- The system rejects the request.

**A4. User did not participate in the ride**

- The system rejects the request.

### Postconditions

- A new rating exists for the ride.
- The user cannot submit another rating for the same ride.

---
# Notifications

## UC-07-01 List Notifications

### Goal

Retrieve system notifications for the authenticated user.

### Primary Actor

Authenticated User

### Preconditions

- The user is authenticated.

### Trigger

The user requests their notifications.

### Main Flow

1. The user requests their notifications.
2. The system validates the access token.
3. The system retrieves the user's notifications.
4. The system returns the notifications.

### Alternative Flows

**A1. Invalid access token**

- The system rejects the request.

### Postconditions

- The user's notifications have been returned.
- Only notifications belonging to the authenticated user are returned.

---
## UC-07-02 Mark Notification as Read

### Goal

Mark a notification as read.

### Primary Actor

Authenticated User

### Preconditions

- The user is authenticated.
- The notification exists.
- The notification belongs to the authenticated user.
- The notification has not already been marked as read.

### Trigger

The user marks a notification as read.

### Main Flow

1. The user selects a notification.
2. The system verifies that the notification belongs to the authenticated user.
3. The system marks the notification as read.
4. The system returns the updated notification.

### Alternative Flows

**A1. Notification not found**

- The system returns an error.

**A2. Notification belongs to another user**

- The system rejects the request.

**A3. Notification is already marked as read**

- The system returns the current notification.

### Postconditions

- The notification is marked as read.