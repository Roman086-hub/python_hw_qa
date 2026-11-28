from sqlalchemy import create_engine, text


db_connection_string = \
    "postgresql://postgres:rzqa2UshYfYZMHZ@localhost:5432/postgres"
db = create_engine(db_connection_string)


def test_add_student():
    connection = db.connect()
    transaction = connection.begin()
    connection.execute(text(
        "INSERT INTO student(user_id) VALUES (:user_id)"),
        {"user_id": "23455"})
    transaction.commit()

    result = connection.execute(
        text("SELECT user_id FROM student WHERE user_id = :user_id"),
        {"user_id": "23455"})
    assert result.scalar() == 23455
    connection.close()


def test_update_student():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("UPDATE student SET level = :lvl WHERE user_id = :id")
    connection.execute(sql, {"lvl": 'update', "id": 23455})
    transaction.commit()

    result = connection.execute(
        text("SELECT level FROM student WHERE user_id = :id"),
        {"id": 23455},
    )
    assert result.scalar() == "update"
    connection.close()


def test_delete_student():
    connection = db.connect()
    transaction = connection.begin()
    sql = text("DELETE FROM student WHERE user_id = :id")
    connection.execute(sql, {"id": 23455})
    transaction.commit()

    result = connection.execute(
        text("SELECT user_id FROM student WHERE user_id = :id"),
        {"id": 23455},
    )
    rows = result.fetchall()
    assert len(rows) == 0
    connection.close()
