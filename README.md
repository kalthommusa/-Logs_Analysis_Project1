# Logs Analysis Project

This is the first project for us as a students of Udacity Full Stack Web Developer Nanodegree program.

## Project Description 

This project is build an internal reporting tool that used information from the database of a newspaper website to answer the following questions in order to analyse the site's user activity.
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

## Project requirements

       - Python 3 
       - PostgreSQL 
       - psycopg 2 library

## Installation

Virtual machine:

  1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) 
  2. Install [Vagrant](https://www.vagrantup.com/downloads.html)
  3. Download [the VM configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
  4. Start the virtual machine:
      - cd vagrant to open the vagrant subdirectory
      - vagrant up to download and install the Linux operating system
      - vagrant ssh to log in to the virtual machine

Database:

  1. Download [the data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
  2. Unzip the archive and move newsdata.sql to the vagrant subdirectory
  3. Within the vagrant subdirectory: psql -d news -f newsdata.sql to initalize the database
  4. Once you have the data loaded into your database, connect to news database using: psql -d news

## Running the project
Once everything is installed: python Logs_Analysis.py

## Project's views

```python
CREATE VIEW top_views AS
SELECT substring(path, 10, 30) AS articles_path, count(*) AS views
FROM log
GROUP BY path
ORDER BY views DESC;
```
```python
CREATE VIEW top_articles AS
SELECT title, views
FROM articles, top_views
WHERE slug = articles_path;
```
```python
CREATE VIEW top_authors AS
SELECT articles.author, sum(views) AS authors_views
FROM articles, top_articles
WHERE articles.title = top_articles.title
GROUP BY articles.author
ORDER BY authors_views DESC;
```
```python
CREATE VIEW daily_view AS
SELECT date(time) AS request_days, count(*) AS views
FROM log 
GROUP BY request_days
ORDER BY request_days DESC;
```
```python
CREATE VIEW daily_error AS
SELECT date(time) AS request_days, count(*) AS errors
FROM log 
WHERE status = '404 NOT FOUND'
GROUP BY request_days 
ORDER BY request_days DESC;
```
```python
CREATE VIEW error_percentage AS
SELECT select daily_view.request_days, 
(100.0*daily_error.errors/daily_view.views) AS percentage
FROM daily_view, daily_error
WHERE daily_view.request_days = daily_error.request_days
ORDER BY percentage DESC;
```