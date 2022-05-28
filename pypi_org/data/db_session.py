import sqlalchemy as sa
import sqlalchemy.orm as orm

factory = None


def global_init(db_file: str):
    global factory

    # if factory has already been called, no need to call it again, so return
    if factory:
        return

    # validate db_file is not whitespace or omitted altogether
    if not db_file or not db_file.strip():
        raise Exception('You must specify a db file.')

    # specify the database type
    connection_str = 'sqlite:///' + db_file.strip()

    # sqlalchemy needs 2 parts: an engine and a factory
    engine = sa.create_engine(connection_str, echo=False)  # set echo=True to see what sqlalchemy is doing

    # Create the session and reference the engine
    factory = orm.sessionmaker(bind=engine)
