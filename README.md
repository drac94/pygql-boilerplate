# Python(Flask), GraphQL(Graphene-SQLAlchemy) and PostgreSQL Boilerplate
This is a boilerplate project for creating a GraphQL API using Flask, PostgreSQL and Graphene-SQLAlchemy as ORM.

## Installing Requirements
### Install pipenv.
```
pip install pipenv
```
### Install the project dependencies
The next command will create a virtualenv and install the dependencies inside
```
pipenv install
```

## Running Flask Server
Go to the root dir and run the below line in the terminal.
```
python app.py
```
## Creating a Database
Create a new postgres database with the table structure mentioned in *pygql.sql* and update the database name in *datastore/dbstore.py* file.
```
dbstore.py

# Replace "postgresql+psycopg2://user@host/dbname" with your path to database

```
## Testing GraphQL
Go to http://localhost:5000/graphql to try GraphQL. Below are the example queries for adding a new post, getting all posts and updating a post.
### Adding a New Post
```
mutation{
  createPost(postData:{title:"title", content:"content"}) {
    post {
      id
      title
      content
    }
  }
}
```
### Getting All Posts 
```
query {
  post {
    id
    title
    content
    createdAt
    updatedAt
  }
}
```

### Updating a Post
```
mutation{
  updatePost(id:"str", title:"new title", content:"new content") {
    post {
      id
      title
      content
    }
  }
}
```

### Deleting a Post
```
mutation{
  deletePost(id:"str") {
    post {
      id
      title
      content
    }
  }
}
```
