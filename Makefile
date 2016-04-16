install:
	sudo pip install requests

run: install
	python3 app.py

clean:
	rm *~
