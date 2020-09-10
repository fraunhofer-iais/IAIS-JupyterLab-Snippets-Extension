all: wheel

install: wheel

	pip uninstall -y snippetlib_jl || true
	jupyter labextension uninstall snippetlib_jl
	pip install dist/snippetlib_jl-*.whl
	jlpm 
	jlpm build 
	jupyter labextension link .
	jlpm build 
	jupyter lab build 
	

Base: 
	git clone https://jira.iais.fraunhofer.de/stash/scm/kdpyt/snippetsbase.git
	cp -r snippetsbase/Base-Snippets/* snippetlib/menu/KD-Snippets/
	

Special: 
	git clone https://jira.iais.fraunhofer.de/stash/scm/kdpyt/snippetsspecial.git
	cp -r snippetsspecial/Special-Snippets/* snippetlib/menu/KD-Snippets/

install_develop: wheel 

	pip uninstall -y snippetlib_jl || true
	pip install dist/snippetlib_jl-*.whl
	

wheel:
	rm -rf build dist
	python setup.py bdist_wheel


install_pipeline: wheel
	pip uninstall -y snippetlib_jl || true
	pip install dist/snippetlib_jl-*.whl



.PHONY: all wheel install


