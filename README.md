# Waterfalls of Oregon API!
### Server side application

Waterfalls of Oregon is a web application that allows a user to view existing waterfall data stored in the database, add new waterfalls to the database, edit existing waterfalls, or delete waterfalls from the database. Note that this app was built with Oregon in mind, but a user can input information for anywhere in the world and the data will be stored correctly and render an icon on the map.

The front end is built with:
- React
- Bootstrap
- Leaflet

[Click here to view the front end repository.](https://github.com/drmeloy/waterfalls-fe)

The back end is built with:
- Django (Python)

The back end is hosted on a Window's provisioned AWS EC2 instance, with the database being ran on an AWS RDS PostgreSQL instance.

### API Endpoints
The API for this server application supports all standard CRUD REST routes of GET, POST, PUT, and DELETE. The base URL for this API is:

`https://ec2-3-23-64-119.us-east-2.compute.amazonaws.com:8000/api/waterfalls`

The REST endpoints are as follows:

##### GET
Get all waterfalls: `<base_url>/`

Get single waterfall by id: `<base_url>/<id>/`

##### POST
Add new waterfall: `<base_url>/`

##### PUT
Update existing waterfall: `<base_url>/<id>/`

##### DELETE
Delete existing waterfall: `<base_url>/<id>/`

### Model schema
The overall JSON shape of the waterfall schema is as follows:
```
{
  "id": <Number>
  "name": <String>,
  "height": <String>,
  "latitude": <String>,
  "longitude": <String>,
  "description": <String>,
  "createdAt": <DateTime>,
  "updatedAt": <DateTime>
}
```
The fields `"id"`, `"createdAt"`, and `"updatedAt"` are handled automatically by the database. The valid JSON shape for creating or updating a waterfall is as follows:
```
{
  "name": <String>,
  "height": <String>,
  "latitude": <String>,
  "longitude": <String>,
  "description": <String>,
}
```

### Connecting and troubleshooting
The web server is hosted on a free tier of AWS EC2. Due to the hardware restrictions of free tier service, API connections may be blocked or interrupted. The web server attempts to provide its self-generated SSL certificate to allow for HTTPS connections, but sometimes the user's browser or hardware settings may warn the user of an untrusted certificate or block the connection entirely. In this situation, the user can attempt to modify proxy and security settings on their system to allow incoming data from untrusted certificates.

# Thank you for using the Waterfalls of Oregon API!