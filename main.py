import psycopg2


class Logs_Analysis:
    def __init__(self, dbname):
        try:
            self.db = psycopg2.connect("dbname=" + dbname)
            self.cursor = self.db.cursor()
        except:
            raise Exception("Uh-oh! Please check your database connections.")

    def print_report(self, question, sql_query, answer):
        # Print the question
        print(question)

        # Execute SQL statement
        self.cursor.execute(sql_query)

        # Print records
        for result in self.cursor:
            print(str(answer).format(result[0], result[1]))

    def __del__(self):
        self.db.close()

logs_analysis = Logs_Analysis("news")

logs_analysis.print_report(
    "1. What are the most popular three articles of all time?",

    """
        SELECT articles.title, COUNT(log.id) AS views
        FROM articles AS articles
        CROSS JOIN log AS log
        WHERE log.path = CONCAT('/article/', articles.slug)
            AND log.status = '200 OK'
        GROUP BY articles.id
        ORDER BY views DESC
        LIMIT 3
    """,

    '\t● "{0}" — {1:,} views'
)

logs_analysis.print_report(
    "\n2. Who are the most popular article authors of all time?",

    """
        SELECT authors.name, COUNT(log.id) AS views
        FROM authors AS authors
        INNER JOIN articles AS articles ON authors.id = articles.author
        CROSS JOIN log AS log
        WHERE log.path = CONCAT('/article/', articles.slug)
            AND log.status = '200 OK'
        GROUP BY authors.name
        ORDER BY views DESC
    """,

    '\t● "{0}" — {1:,} views'
)

logs_analysis.print_report(
    "\n3. On which days did more than 1% of requests lead to errors?",

    """
        SELECT all_logs.day, ROUND(
            error_logs.views::NUMERIC * 100 / all_logs.views::NUMERIC, 2
        ) AS error

        FROM (
            SELECT DATE(time) AS day, COUNT(id) AS views
            FROM log
            GROUP BY day
        ) AS all_logs

        INNER JOIN (
            SELECT DATE(time) AS day, COUNT(id) AS views
            FROM log
            WHERE status = '404 NOT FOUND'
            GROUP BY day
        ) AS error_logs ON all_logs.day = error_logs.day

        WHERE ROUND(
            error_logs.views::NUMERIC * 100 / all_logs.views::NUMERIC, 2
        ) > 1.00

        ORDER BY error DESC
        LIMIT 1
    """,

    "\t● {0:%B %d, %Y} - {1}% errors"
)

del logs_analysis
