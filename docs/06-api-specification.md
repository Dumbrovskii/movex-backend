# API Specification

**Document ID:** API-001  
**Product:** MoveX  
**Version:** 1.0  
**Status:** Draft

---

# Introduction

This document defines the public REST API exposed by the MoveX backend.

The API is based on the business requirements and use cases described in the project documentation.

All request and response bodies use JSON unless stated otherwise.

---

# Conventions

## Base URL

```text
/api/v1
```

## Authentication

Protected endpoints require a valid JWT access token.

```http
Authorization: Bearer <access_token>
```

## Content Type

```http
Content-Type: application/json
```

## Date and Time

All date and time values use the ISO 8601 format in UTC.

Example:

```text
2026-08-02T18:45:00Z
```

## Resource Identifiers

All resources use BIGINT identifiers.

Example:

```text
6a5eb9d6-f84f-45c6-bf3b-8df6f1c98d77
```

## HTTP Status Codes

| Code | Description |
|------|-------------|
|200|OK|
|201|Created|
|204|No Content|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|
|409|Conflict|
|422|Validation Error|
|500|Internal Server Error|

---

# Authentication

## POST /auth/request-code

### Description

Requests a one-time verification code for the specified phone number.

### Authentication

Not required.

### Request

```json
{
  "phone": "+380991234567"
}
```

### Responses

#### 200 OK

```json
{
  "message": "Verification code sent."
}
```

#### 400 Bad Request

```json
{
  "error": {
    "code": "INVALID_PHONE_NUMBER",
    "message": "Invalid phone number."
  }
}
```

#### 429 Too Many Requests

```json
{
  "error": {
    "code": "TOO_MANY_REQUESTS",
    "message": "Too many requests."
  }
}
```

---

## POST /auth/verify

### Description

Verifies the submitted verification code.

If the user does not exist, a new user account is created automatically.

### Authentication

Not required.

### Request

```json
{
  "phone": "+380991234567",
  "code": "123456"
}
```

### Responses

#### 200 OK

```json
{
  "access_token": "<jwt>",
  "refresh_token": "<refresh_token>",
  "token_type": "Bearer",
  "expires_in": 900
}
```

#### 400 Bad Request

```json
{
  "error": {
    "code": "INVALID_VERIFICATION_CODE",
    "message": "Invalid verification code."
  }
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "VERIFICATION_CODE_EXPIRED",
    "message": "Verification code expired."
  }
}
```

---

## POST /auth/refresh

### Description

Issues a new access token using a valid refresh token.

### Authentication

Not required.

### Request

```json
{
  "refresh_token": "<refresh_token>"
}
```

### Responses

#### 200 OK

```json
{
  "access_token": "<jwt>",
  "token_type": "Bearer",
  "expires_in": 900
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "INVALID_REFRESH_TOKEN",
    "message": "Invalid or expired refresh token."
  }
}
```

---

## POST /auth/logout

### Description

Removes the specified refresh token from Redis.

### Authentication

Required.

### Request

```json
{
  "refresh_token": "<refresh_token>"
}
```

### Responses

#### 204 No Content

---

# Users

## GET /users/me

### Description

Returns the authenticated user's profile.

### Authentication

Required.

### Request

None.

### Responses

#### 200 OK

```json
{
  "id": "6a5eb9d6-f84f-45c6-bf3b-8df6f1c98d77",
  "phone": "+380991234567",
  "full_name": "John Doe",
  "email": "john.doe@example.com",
  "created_at": "2026-08-02T18:45:00Z",
  "updated_at": "2026-08-02T18:45:00Z"
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

---

## PATCH /users/me

### Description

Updates the authenticated user's profile.

Only the supported fields may be updated.

### Authentication

Required.

### Request

```json
{
  "full_name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Responses

#### 200 OK

```json
{
  "id": "6a5eb9d6-f84f-45c6-bf3b-8df6f1c98d77",
  "phone": "+380991234567",
  "full_name": "John Doe",
  "email": "john.doe@example.com",
  "created_at": "2026-08-02T18:45:00Z",
  "updated_at": "2026-08-02T18:50:12Z"
}
```

#### 400 Bad Request

```json
{
  "error": {
    "code": "INVALID_PROFILE_DATA",
    "message": "The submitted profile data is invalid."
  }
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

---

# Drivers

## GET /drivers/me

### Description

Returns the authenticated user's driver profile.

### Authentication

Required.

### Request

None.

### Responses

#### 200 OK

```json
{
  "id": "6a5eb9d6-f84f-45c6-bf3b-8df6f1c98d77",
  "status": "Verified",
  "created_at": "2026-08-02T18:45:00Z",
  "updated_at": "2026-08-02T18:50:00Z"
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 404 Not Found

```json
{
  "error": {
    "code": "DRIVER_NOT_FOUND",
    "message": "Driver profile not found."
  }
}
```

---

## POST /drivers

### Description

Creates a driver profile for the authenticated user.

### Authentication

Required.

### Request

```json
{}
```

### Responses

#### 201 Created

```json
{
  "id": "6a5eb9d6-f84f-45c6-bf3b-8df6f1c98d77",
  "status": "Pending",
  "created_at": "2026-08-02T18:45:00Z",
  "updated_at": "2026-08-02T18:45:00Z"
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "DRIVER_ALREADY_EXISTS",
    "message": "Driver profile already exists."
  }
}
```

---

# Rides

## POST /rides

### Description

Creates a new ride request.

### Authentication

Required.

### Request

```json
{
  "pickup_address": "Khreshchatyk St, 22, Kyiv",
  "pickup_geo": {
    "latitude": 50.450001,
    "longitude": 30.523333
  },
  "destination_address": "Boryspil International Airport",
  "destination_geo": {
    "latitude": 50.345001,
    "longitude": 30.894722
  }
}
```

### Responses

#### 201 Created

```json
{
  "id": "8b9d2cb3-27f7-48c8-8e4b-11c10d1ef8db",
  "status": "Requested",
  "passenger_id": "6a5eb9d6-f84f-45c6-bf3b-8df6f1c98d77",
  "pickup_address": "Khreshchatyk St, 22, Kyiv",
  "destination_address": "Boryspil International Airport",
  "created_at": "2026-08-02T18:45:00Z"
}
```

#### 400 Bad Request

```json
{
  "error": {
    "code": "INVALID_RIDE_DATA",
    "message": "The submitted ride data is invalid."
  }
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "ACTIVE_RIDE_EXISTS",
    "message": "An active ride already exists."
  }
}
```

---

## POST /rides/{ride_id}/accept

### Description

Assigns the authenticated driver to the specified ride.

### Authentication

Required.

### Request

None.

### Responses

#### 200 OK

```json
{
  "id": "8b9d2cb3-27f7-48c8-8e4b-11c10d1ef8db",
  "driver_id": "6a5eb9d6-f84f-45c6-bf3b-8df6f1c98d77",
  "status": "Accepted"
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 403 Forbidden

```json
{
  "error": {
    "code": "DRIVER_NOT_VERIFIED",
    "message": "Driver is not verified."
  }
}
```

#### 404 Not Found

```json
{
  "error": {
    "code": "RIDE_NOT_FOUND",
    "message": "Ride not found."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "RIDE_ALREADY_ACCEPTED",
    "message": "Ride has already been accepted."
  }
}
```

---

## POST /rides/{ride_id}/cancel

### Description

Cancels the specified ride.

### Authentication

Required.

### Request

None.

### Responses

#### 200 OK

```json
{
  "id": "8b9d2cb3-27f7-48c8-8e4b-11c10d1ef8db",
  "status": "Cancelled"
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 404 Not Found

```json
{
  "error": {
    "code": "RIDE_NOT_FOUND",
    "message": "Ride not found."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "RIDE_CANNOT_BE_CANCELLED",
    "message": "Ride cannot be cancelled."
  }
}
```

---

## POST /rides/{ride_id}/start

### Description

Starts the specified ride.

### Authentication

Required.

### Request

None.

### Responses

#### 200 OK

```json
{
  "id": "8b9d2cb3-27f7-48c8-8e4b-11c10d1ef8db",
  "status": "InProgress"
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 404 Not Found

```json
{
  "error": {
    "code": "RIDE_NOT_FOUND",
    "message": "Ride not found."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "INVALID_RIDE_STATUS",
    "message": "Ride cannot be started."
  }
}
```

---

## POST /rides/{ride_id}/complete

### Description

Completes the specified ride.

### Authentication

Required.

### Request

None.

### Responses

#### 200 OK

```json
{
  "id": "8b9d2cb3-27f7-48c8-8e4b-11c10d1ef8db",
  "status": "Completed"
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 404 Not Found

```json
{
  "error": {
    "code": "RIDE_NOT_FOUND",
    "message": "Ride not found."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "INVALID_RIDE_STATUS",
    "message": "Ride cannot be completed."
  }
}
```

---

# Payments

## POST /payments

### Description

Creates a payment for a completed ride.

### Authentication

Required.

### Request

```json
{
  "ride_id": "8b9d2cb3-27f7-48c8-8e4b-11c10d1ef8db",
  "amount": "350.00",
  "currency": "UAH"
}
```

### Responses

#### 201 Created

```json
{
  "id": "3c4f6d89-18fd-4e17-8b26-48c32e61358a",
  "ride_id": "8b9d2cb3-27f7-48c8-8e4b-11c10d1ef8db",
  "amount": "350.00",
  "currency": "UAH",
  "status": "Pending",
  "created_at": "2026-08-02T18:45:00Z"
}
```

#### 400 Bad Request

```json
{
  "error": {
    "code": "INVALID_PAYMENT_DATA",
    "message": "The submitted payment data is invalid."
  }
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 404 Not Found

```json
{
  "error": {
    "code": "RIDE_NOT_FOUND",
    "message": "Ride not found."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "RIDE_NOT_COMPLETED",
    "message": "Ride has not been completed."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "PAYMENT_ALREADY_EXISTS",
    "message": "Payment already exists for this ride."
  }
}
```

---

# Ratings

## POST /ratings

### Description

Creates a rating for a completed ride.

### Authentication

Required.

### Request

```json
{
  "ride_id": "8b9d2cb3-27f7-48c8-8e4b-11c10d1ef8db",
  "target_user_id": "95d4c6c5-ef6a-4d52-8d9b-f2b4d9c65b44",
  "score": 5,
  "comment": "Excellent ride!"
}
```

### Responses

#### 201 Created

```json
{
  "id": "5ab12a1d-66d5-4d0d-98d7-d9dca23f8b1b",
  "ride_id": "8b9d2cb3-27f7-48c8-8e4b-11c10d1ef8db",
  "author_user_id": "6a5eb9d6-f84f-45c6-bf3b-8df6f1c98d77",
  "target_user_id": "95d4c6c5-ef6a-4d52-8d9b-f2b4d9c65b44",
  "score": 5,
  "comment": "Excellent ride!",
  "created_at": "2026-08-02T18:45:00Z"
}
```

#### 400 Bad Request

```json
{
  "error": {
    "code": "INVALID_RATING_DATA",
    "message": "The submitted rating data is invalid."
  }
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 403 Forbidden

```json
{
  "error": {
    "code": "USER_NOT_PARTICIPANT",
    "message": "The user did not participate in this ride."
  }
}
```

#### 404 Not Found

```json
{
  "error": {
    "code": "RIDE_NOT_FOUND",
    "message": "Ride not found."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "RIDE_NOT_COMPLETED",
    "message": "Ride has not been completed."
  }
}
```

#### 409 Conflict

```json
{
  "error": {
    "code": "RATING_ALREADY_EXISTS",
    "message": "A rating has already been submitted for this ride."
  }
}
```

---

# Notifications

## GET /notifications

### Description

Returns the authenticated user's notifications.

### Authentication

Required.

### Request

None.

### Responses

#### 200 OK

```json
[
  {
    "id": "c7b17e18-ec2f-46d0-84f7-64d99f4d4d5d",
    "type": "RideAccepted",
    "title": "Ride accepted",
    "message": "Your ride has been accepted by a driver.",
    "is_read": false,
    "created_at": "2026-08-02T18:45:00Z"
  },
  {
    "id": "3b0f6f07-8d07-43d5-b91f-725fc38bde47",
    "type": "RideCompleted",
    "title": "Ride completed",
    "message": "Your ride has been completed.",
    "is_read": true,
    "created_at": "2026-08-01T17:30:00Z"
  }
]
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

---

## PATCH /notifications/{notification_id}/read

### Description

Marks the specified notification as read.

### Authentication

Required.

### Request

None.

### Responses

#### 200 OK

```json
{
  "id": "c7b17e18-ec2f-46d0-84f7-64d99f4d4d5d",
  "is_read": true,
  "updated_at": "2026-08-02T18:50:00Z"
}
```

#### 401 Unauthorized

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required."
  }
}
```

#### 403 Forbidden

```json
{
  "error": {
    "code": "NOTIFICATION_ACCESS_DENIED",
    "message": "The notification does not belong to the authenticated user."
  }
}
```

#### 404 Not Found

```json
{
  "error": {
    "code": "NOTIFICATION_NOT_FOUND",
    "message": "Notification not found."
  }
}
```