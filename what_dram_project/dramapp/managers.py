from django.db import connection


def top_rated(self):
    from dramapp.models import Rating

    subquery = "SELECT SUM(%(rating_column)s) from %(rating_table)s WHERE%(rating_table)s.%(whisky_column)s = whisky.id"
    params = {'rating_column': connection.ops.quote_name('rating'),
              'rating_table': connection.ops.quote_name(Rating._meta.db_table),
              'whisky_column': connection.ops.quote_name('whisky_id')}
    return self.extra(select={'score': subquery % params},
                      order_by=['-score'])