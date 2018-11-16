#!/usr/bin/env python3
#Log Analysis Project 1 for Full Stack Nanodegree by Udacity

import psycopg2


def main():
    # Connect to the database
    conn = psycopg2.connect("dbname=news")

    # Open a cursor 
    db_cursor = conn.cursor()

    # Question 1
    sql_popular_3_articles = """
      SELECT *
      FROM top_articles
      LIMIT 3;
    """
    db_cursor.execute(sql_popular_3_articles)
    results = db_cursor.fetchall()
    print("1. What are the most popular three articles of all time ?")
    print("")
    for result in results:
        print('   "{title}" - {views} views'
              .format(title=result[0], views=result[1]))
    print("_____________________________________________________________")
    print("")

    # Question 2
    sql_popular_authors = """
    SELECT authors.name , top_authors.authors_views
    FROM authors, top_authors
    WHERE authors.id = top_authors.author;
    """
    db_cursor.execute(sql_popular_authors)
    results = db_cursor.fetchall()
    print("2. Who are the most popular article authors of all time?")
    print("")
    for result in results:
        print('   {name} - {authors_views} views'
              .format(name=result[0], authors_views=result[1]))
    print("_____________________________________________________________")
    print("")

    # Question 3
    sql_more_than_one_percent_errors = """
    SELECT to_char (request_days, 'Mon dd ,YYYY') AS request_day, to_char(percentage,'999D99%') AS error_percentage
    FROM error_percentage
    WHERE error_percentage.percentage > 1;
    """
    db_cursor.execute(sql_more_than_one_percent_errors)
    results = db_cursor.fetchall()
    print("3. On which days did more than 1% of requests lead to errors?")
    print("")
    for result in results:
        print('   {request_days} - {percentage} errors'
              .format(request_days=result[0], percentage=result[1]))        
    print("_____________________________________________________________")
    print("")

    # Close communication with the database
    db_cursor.close()
    conn.close()

if __name__ == "__main__":
    main()