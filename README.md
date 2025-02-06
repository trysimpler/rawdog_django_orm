# Rawdog django ORM

The django ORM and CRM provide amazing interfaces that work out of the box and have the most pleasant and advnaced migration system I've ever encountered.

Their core flaw is that they are designed to work with django, and thus suffer from constraints around:
- Async/io usage
- Performance
- Sane design patterns

This package contains various utilities I need in order to use the django ORM and admin UI inside modern projects.

I'm making it public in case others find it useful.

