## -----------DAY-10----------08 August 2026--------------------------------

1. What is FastAPI?
    FastAPI is a modern Python web framework used to build APIs.
    It provides the tools and features needed to create fast, scalable web APIs efficiently.  

    ===========             ===========      request     ===========             
    | Web Appln|   =====>   | FastAPI  |   ==========>  | Database  |
    |    OR    |            |          |   <==========  | Engine    |
    |Swagger UI|            ------------     response   -------------
     ----------             

2. What is an API?
    API stands for Application Programming Interface.
    It is a communication interface.
    It allows different software applications or systems to communicate with each other.

3. What is an endpoint?
    An endpoint is a specific URL/path through which an API provides access to a particular
    resource or functionality.
    Examples:
        /products
        /users
        /orders

4. What are the common HTTP methods?
    - GET - retrieves data from the server.
    - POST - creates or sends new data to the server.
    - PUT - updates existing data.
    - DELETE - deletes data from the server.

        | Method   | Purpose              |
        | -------- | -------------------- |
        | `GET`    | Retrieve data        |
        | `POST`   | Create/send new data |
        | `PUT`    | Update data          |
        | `DELETE` | Delete data          |

5. What is the difference between an API and an endpoint?
    - API - a way for different software applications or systems to communicate with each other.
    - Endpoint - a specific URL/path through which a particular API functionality can be accessed.

6. What does GET /products mean?
    GET - HTTP method used to retrieve data.
    # (HTTP (Hypertext Transfer Protocol) is a core Internet protocol that defines how data is exchanged between clients and servers on the web)
    /products - endpoint/path used to access product-related data.

    