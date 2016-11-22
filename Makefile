.PHONY: run
run: tictactoe/Application.py
	python tictactoe/Application.py

test:
	python -m unittest discover -v
