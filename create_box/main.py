def create_box(height, width, character):
  box_list = [[character for i in range(width)]for j in range(height)]
  box = ""
  for i in range(height):
    for j in range(width):
      box += box_list[i][j]
    box += "\n"
  return box



# Tests:

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected

def test_third_box():
    assert create_box(3, 24, 'x') == third_box_expected