# Python(Flask), GraphQL(Graphene-SQLAlchemy) and PostgreSQL Boilerplate
This is a boilerplate project for creating a GraphQL API using Flask, PostgreSQL and Graphene-SQLAlchemy as ORM.

## Table of Contents

- [Software Requirements](#software-requirements)
- [Installing Requirements](#installing-requirements)
- [Creating a Database](#creating-a-database)
- [Running Flask Server](#running-flask-server)
- [Unit Tests](#unit-tests)
- [Other Scripts](#other-scripts)

## Software Requirements

| Third-party Dependency |      Description      | 
|----------|-------------|
| [postgres](https://www.postgresql.org/) | Database.|
| [git](https://git-scm.com/downloads) | Code Version Control tool.|
| [python](https://www.python.org/) |  Programming language, version 3.7 or grater. | 
| [pip](https://pypi.org/project/pip/) |  Dependency Management tool.  |

[⇧ back to top](#table-of-contents)

## Installing Requirements
### Install pipenv.
```
pip install pipenv
```

### Install project dependencies
```
pipenv install --dev
```
The previous command will create a virtualenv and install the dependencies inside

[⇧ back to top](#table-of-contents)

## Creating a Database
Create a new postgres database with the table structure mentioned in **pygql.sql**, then, create an `.env` file following the `.env.example`  and set the name, user, host and password of your database.

[⇧ back to top](#table-of-contents)


## Running Flask Server
Go to the root dir and run the below line in the terminal.
```
pipenv run dev
```

[⇧ back to top](#table-of-contents)

## Testing GraphQL
Go to http://localhost:5000/graphql to try GraphQL. Below are the example queries for adding a new post, getting all posts, getting, updating and deleting a post.
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
{
  posts {
    id
    title
    content
    createdAt
    updatedAt
  }
}
```

### Getting a Post by ID
```
{
  post(id:"uuid") {
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

[⇧ back to top](#table-of-contents)

## Unit Tests
To run the unit tets, create an empty database, duplicate the `.env` file and rename it to `.env.test`, then replace the POSTGRES_DB variable with the name of your test database.

> IMPORTANT: Running the test command without doing the previous step or running pytest standalone will clear your main database.

Now, run the next command
```
pipenv run test
```

[⇧ back to top](#table-of-contents)

## Other Scripts
### Format Code
```
pipenv run format
```

### Lint Check
```
pipenv run lint
```

[⇧ back to top](#table-of-contents)