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
pipenv run dev
```
## Creating a Database
Create a new postgres database with the table structure mentioned in *pygql.sql*, create an `.env` file and set the database name, user, host and password

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

## Unit Tests
To run the unit tets you need to create an empty database and an env file called `.env.test` with the same variables as the `.env` file, then add the name of your test database to the env file and run the command

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