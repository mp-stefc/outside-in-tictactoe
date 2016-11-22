.PHONY: run
run: tictactoe/Application.py
	python $<

test:
	python -m unittest discover -v
