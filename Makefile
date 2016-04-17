install:
	sudo pip3 install requests tinydb flask

run: install
	python3 app.py

clean:
	rm *~
