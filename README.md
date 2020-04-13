# Python(Flask), GraphQL(Graphene-SQLAlchemy) and PostgreSQL Boilerplate
This is a boilerplate project for creating a GraphQL API using Flask, PostgreSQL and Graphene-SQLAlchemy as ORM.

## Installing Requirements
### Install pipenv.
```
pip install pipenv
```

### Install project dependencies
```
pipenv install
```
The previous command will create a virtualenv and install the dependencies inside

## Creating a Database
Create a new postgres database with the table structure mentioned in **pygql.sql**, then, create an `.env` file following the `.env.example`  and set the name, user, host and password of your database.


## Running Flask Server
Go to the root dir and run the below line in the terminal.
```
pipenv run dev
```

## Testing GraphQL
Go to http://localhost:5000/graphql to try GraphQL. Below are the example queries for adding a new post, getting all posts, updating and deleting a post.
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
  allPosts {
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
  updatePost(id:"uuid", title:"new title", content:"new content") {
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
  deletePost(id:"uuid") {
    post {
      id
      title
      content
    }
  }
}
```

## Unit Tests
To run the unit tets, create an empty database, duplicate the `.env` file and rename it to `.env.test`, then replace the POSTGRES_DB variable with the name of your test database.

Now, run the next command
```
pipenv run test
```

## Other Scripts
### Format Code
```
pipenv run format
```

### Lint Check
```
pipenv run lint
```