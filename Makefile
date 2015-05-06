env:
	virtualenv --distribute --no-site-packages env

install: env
	env/bin/pip install -r requirements/production.txt

clean:
	git clean -fXd
