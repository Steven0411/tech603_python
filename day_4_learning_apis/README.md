# APIs

## What is an API?

* Interface for software/services to be able to talk to each other
* gives access to:
  * data 
  * images
  * videos
  * web pages
* allow to ask for an action to be done

## Why DevOps engineers need to use APIs

* (automate) interactions with cloud services
* integrate and manage DevOps tools and platforms
* retrieve and manipulate from external systems

## RESTful services

* REST - representational state transfer
* type of architecture used for api
* primarily used to build wev services which are lightweight, maintainable and scalable
* RESTful services use HTTP

RESTful services should have the following properties:
* Representation and data flow
* messages
* URIs / naming resources
* statelessness
* caching

## HTTP messages and verbs

* HTTP is the protocol for internet communication
* HTTPS is the secure/enrypted version

| HTTP Verb | 	CRUD                                                 |
|-----------|-------------------------------------------------------|
| POST      | Create                                                |
| GET       | 	Read 	                                               |
| PUT       | Update: Complete replacement of a particular record 	 |
| PATCH     | Update: Modify a specific piece of data 	             |
| DELETE    | 	Delete                                               |

## HTTPs request structure

* Verb URL Version
* eg GET HTTP://example.com 1.1

## HTTP response structure

* response code HTTP Version
* eg 200 v1.1 

## statelessness

request contains all information needed to process it

## caching

* saves certain pieces of a request sto prevent having to load it each time
* streamlines and speeds up certain processes