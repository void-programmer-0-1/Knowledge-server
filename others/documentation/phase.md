
v1: (1 week time)

    User registration, login, logout.
    JWT authentication (stateless, secure).
    Role-based access (admin vs. user).
    
    Create, read, update, delete notes.
    Organize with tags and categories.
    Keep history/versions of notes.
    Soft delete (trash bin) instead of permanent delete.

    API versioning: e.g., /api/v1/notes/.
    OpenAPI/Swagger docs: Auto-generated API documentation.

v2: (1 week)

    Nginx for load balancer
    Docker
    Postgres
    Deployment in aws ec2
    Attach files/images to notes (stored in S3).
    Secure upload via pre-signed URLs.
    Rate limiting: Prevent abuse of API.

v3: (1 week)

    Search notes by text/tags/dates.
    Background tasks for indexing (Celery + Redis).
    Caching: Frequently requested data via Redis.
    Pagination: Efficient API responses for large datasets.

v4:

    Number of notes created per day/week/month.
    Most-used tags.
    User activity stats (active users, recently edited notes).

v5:

    Share a note with another user (permissions: read-only, read-write).
    Public links (with expiration tokens).
    Notifications when a note is shared.
    (Future) Real-time editing via WebSockets.
