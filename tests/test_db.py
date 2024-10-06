from olympics import db


def test_athletes():
    rows = db.get_athletes()
    assert len(rows) > 160


def test_disciplines():
    rows = db.get_disciplines()
    assert len(rows) > 40


def test_teams():
    rows = db.get_teams()
    assert len(rows) > 100


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 150


def test_countries_id():
    rows = db.get_countries(1)
    assert len(rows) == 1


def test_athletes_id():
    rows = db.get_athletes(1)
    assert len(rows) == 1


def test_disciplines_id():
    rows = db.get_disciplines(1)
    assert len(rows) == 1


def test_teams_id():
    rows = db.get_teams(1)
    assert len(rows) == 1


def test_events():
    rows = db.get_events()
    assert len(rows) > 100


def test_events_id():
    rows = db.get_events(1)
    assert len(rows) == 1


def test_medals():
    rows = db.get_medals()
    assert len(rows) > 100


def test_medals_id():
    rows = db.get_medals(1)
    assert len(rows) == 1


def test_discipline_athletes():
    rows = db.get_discipline_athletes(1)
    assert len(rows) > 0


def test_top_countries():
    rows = db.get_top_countries(10)
    assert len(rows) == 10


def test_collective_medals():
    rows = db.get_collective_medals()
    assert len(rows) > 100


def test_collective_medals_id():
    rows = db.get_collective_medals(1)
    assert len(rows) > 0


def test_top_collective():
    rows = db.get_top_collective(10)
    assert len(rows) == 10


def test_individual_medals():
    rows = db.get_individual_medals()
    assert len(rows) > 100


def test_individual_medals_id():
    rows = db.get_individual_medals(1)
    assert len(rows) == 1


def test_top_individual():
    rows = db.get_top_individual(10)
    assert len(rows) == 10


def test_get_connection():
    conn = db.get_connection()
    assert conn is not None
    conn.close()


def test_get_countries_no_id():
    rows = db.get_countries()
    assert len(rows) > 0


def test_get_athletes_no_id():
    rows = db.get_athletes()
    assert len(rows) > 0


def test_get_disciplines_no_id():
    rows = db.get_disciplines()
    assert len(rows) > 0


def test_get_teams_no_id():
    rows = db.get_teams()
    assert len(rows) > 0


def test_get_events_no_id():
    rows = db.get_events()
    assert len(rows) > 0


def test_get_medals_no_id():
    rows = db.get_medals()
    assert len(rows) > 0


def test_get_discipline_athletes_no_id():
    rows = db.get_discipline_athletes(1)
    assert len(rows) > 0


def test_get_top_countries():
    rows = db.get_top_countries()
    assert len(rows) >= 10


def test_get_collective_medals_no_id():
    rows = db.get_collective_medals()
    assert len(rows) > 0


def test_get_top_collective_no_top():
    rows = db.get_top_collective()
    assert len(rows) == 10


def test_get_individual_medals_no_id():
    rows = db.get_individual_medals()
    assert len(rows) > 0


def test_get_top_individual_no_top():
    rows = db.get_top_individual()
    assert len(rows) == 10
