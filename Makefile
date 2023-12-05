all: one two

one:

	python /home/student/git_repo/sdn_dumps/script_fetch.py 
two:
	bash /home/student/git_repo/sdn_dumps/git_push.sh
