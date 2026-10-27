from unittest.mock import patch

inputs = ["1", "1", "2026-10-27"]

with patch("builtins.input", side_effect=inputs):
    movie_id = input("Enter Movie ID: ")
    screen = input("Enter Screen: ")
    show_date = input("Enter Show Date: ")

print(movie_id, screen, show_date)