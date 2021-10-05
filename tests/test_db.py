from bot.db import schema

conn = schema.create_connection(schema.DATABASE_PATH)

# answer, warning, question = schema.main(
#         randrange(0, 19), randrange(0, 4), randrange(0, 1),
#     )


def test_create_connection():
    actual = schema.create_connection(schema.DATABASE_PATH)
    expected = 'Error Establishing a Database Connection'
    assert actual is not expected


def test_select_answer():
    actual = schema.select_answer(conn, 0)
    expected = 'Мне кажется — «да».'
    assert actual == expected


def test_select_warning():
    actual = schema.select_warning(conn, 0)
    expected = 'Знаете, шар — это, конечно, хорошо, но он знает не всё.'
    assert actual == expected


def test_select_question():
    actual = schema.select_question(conn, 0)
    expected = 'Хотите спросить что-нибудь ещё?'
    assert actual == expected
