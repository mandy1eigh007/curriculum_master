# Server-Side Programming

## Required Hours
- **Total Hours**: 20 hours
- **Session Pattern**: 5 sessions of 4 hours each

## Purpose

Server-side programming powers the backend of web applications, handling business logic, data processing, and database operations. This module introduces fundamental concepts of backend development that apply across languages and frameworks.

## Learning Outcomes

Students will be able to:

- Understand client-server architecture and HTTP protocol
- Build basic server applications handling requests and responses
- Implement routing for different application endpoints
- Work with databases to store and retrieve data
- Apply security best practices for server-side code

## Core Content

### Client-Server Architecture

How web applications work:

**Request-Response Cycle**:
- Client sends HTTP request
- Server processes and responds
- Stateless communication
- Request methods: GET, POST, PUT, DELETE
- Response status codes: 200, 404, 500, etc.

**HTTP Protocol**:
- Headers and their purposes
- Request and response bodies
- Content types and MIME types
- Cookies and sessions
- HTTPS and encryption

### Server Basics

Creating server applications:

**Server Setup**:
- Initializing a server application
- Listening on ports
- Handling incoming connections
- Environment variables and configuration
- Logging and monitoring

**Request Handling**:
- Parsing request data
- Query parameters and URL parsing
- Request body parsing: JSON, form data
- File uploads
- Error handling and validation

### Routing

Directing requests to appropriate handlers:

**Route Definition**:
- URL patterns and matching
- Dynamic route parameters
- Query string parameters
- Route organization and structure
- RESTful routing conventions

**HTTP Methods**:
- GET for reading data
- POST for creating data
- PUT/PATCH for updating data
- DELETE for removing data
- Method override for compatibility

### Database Integration

Storing and retrieving persistent data:

**Database Concepts**:
- Relational vs non-relational databases
- Tables, rows, and columns
- Primary keys and foreign keys
- Indexes for performance
- Database connections and pooling

**CRUD Operations**:
- Create: Inserting new records
- Read: Querying existing data
- Update: Modifying records
- Delete: Removing records
- Filtering, sorting, and pagination

**SQL Basics**:
- SELECT statements and WHERE clauses
- INSERT, UPDATE, DELETE
- JOIN operations
- Aggregate functions: COUNT, SUM, AVG
- Transaction basics

### Template Rendering

Generating dynamic HTML:

**Server-Side Templates**:
- Template syntax and variables
- Conditionals in templates
- Loops for collections
- Partials and layouts
- Data passing to templates

**Dynamic Content**:
- Rendering data from database
- User-specific content
- Forms and CSRF protection
- Flash messages
- Error displays

### Authentication and Authorization

Securing applications:

**Authentication**:
- User registration and login
- Password hashing (never store plain text)
- Session management
- Token-based authentication
- Logout functionality

**Authorization**:
- Checking user permissions
- Role-based access control
- Protecting routes
- Resource ownership verification
- Middleware for auth checks

### API Development Basics

Creating programmatic interfaces:

**RESTful APIs**:
- Resource-based URLs
- Standard HTTP methods
- JSON request and response bodies
- Status codes for API responses
- API versioning considerations

**API Best Practices**:
- Consistent naming conventions
- Proper error messages
- Input validation
- Rate limiting awareness
- Documentation

### Security Best Practices

Protecting applications and users:

**Common Vulnerabilities**:
- SQL injection prevention
- Cross-site scripting (XSS) protection
- Cross-site request forgery (CSRF) tokens
- Input validation and sanitization
- Secure password storage

**General Security**:
- HTTPS and secure connections
- Environment variables for secrets
- Dependency security updates
- Error message information disclosure
- Secure headers

## Deliverables

- Server application with multiple routes
- Database integration with CRUD operations
- User authentication and protected routes
- RESTful API with documentation
- Security measures implemented and documented
