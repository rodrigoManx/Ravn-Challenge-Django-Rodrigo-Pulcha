## Setup and running instructions

You must have docker installed
1. Download or clonde this repository
2. Enter repository main folder
3. Run in a terminal `docker-compose up`

## Project description

This project is a web application that consumes the Star Wars GraphQL Api, using django as framework backend, to list some of the nodes present in the graph, such as people and spaceships, as well as the details of each of these nodes.

## Screen captures
<p float="left">
<img src="https://raw.githubusercontent.com/rodrigoManx/Ravn-Challenge-Django-Rodrigo-Pulcha/master/static/screenCaptures/sc1.jpg" width="250">
<img src="https://raw.githubusercontent.com/rodrigoManx/Ravn-Challenge-Django-Rodrigo-Pulcha/master/static/screenCaptures/sc2.jpg" width="250">
<img src="https://raw.githubusercontent.com/rodrigoManx/Ravn-Challenge-Django-Rodrigo-Pulcha/master/static/screenCaptures/sc3.jpg" width="250">
<img src="https://raw.githubusercontent.com/rodrigoManx/Ravn-Challenge-Django-Rodrigo-Pulcha/master/static/screenCaptures/sc4.jpg" width="250">
<img src="https://raw.githubusercontent.com/rodrigoManx/Ravn-Challenge-Django-Rodrigo-Pulcha/master/static/screenCaptures/fsc5.jpg" width="250">
<img src="https://raw.githubusercontent.com/rodrigoManx/Ravn-Challenge-Django-Rodrigo-Pulcha/master/static/screenCaptures/sc6.jpg" width="250">
</p>

## Assumptions

Although this is a web application, it is oriented and optimized for mobile devices since they are used more frequently to access the internet in people's daily lives, than for example a personal computer

Two approaches were used, both do the same, but the first one uses a a Restful API using Django REST Framework over an SQL scheme and second one uses a GRAPHQL scheme, first one can be accessed from base url http://localhost:8000 and the second one from http://localhost:8000/graphql-mode/

## Technologies used

1. React Js Framework
