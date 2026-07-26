## Datastore Connect

A high performance core database driver for connecting Datastore to Python, Pandas, and Superset

* Pandas DataFrames
* Numpy Arrays
* PyArrow Tables
* Superset Connector
* SQLAlchemy 1.3 and 1.4 (limited feature set)

Datastore Connect currently uses the Datastore HTTP interface for maximum compatibility.

### Installation

```
pip install datastore-connect
```

Datastore Connect requires Python 3.8 or higher.

### Superset Connectivity

Datastore Connect is fully integrated with Apache Superset. Previous versions of Datastore Connect utilized a
dynamically loaded Superset Engine Spec, but as of Superset v2.1.0 the engine spec was incorporated into the main
Apache Superset project and removed from datastore-connect in v0.6.0. If you have issues connecting to earlier
versions of Superset, please use datastore-connect v0.5.25.

When creating a Superset Data Source, either use the provided connection dialog, or a SqlAlchemy DSN in the form
`datastoredb://{username}:{password}@{host}:{port}`.

### SQLAlchemy Implementation

Datastore Connect incorporates a minimal SQLAlchemy implementation (without any ORM features) for compatibility with
Superset. It has only been tested against SQLAlchemy versions 1.3.x and 1.4.x, and is unlikely to work with more
complex SQLAlchemy applications.

### Asyncio Support

Datastore Connect provides an async wrapper, so that it is possible to use the client in an `asyncio` environment.
See the [run_async example](./examples/run_async.py) for more details.

### Complete Documentation

The documentation for Datastore Connect has moved to
[Datastore Docs](https://docs.hanzo.ai/datastore/integrations/python) 
