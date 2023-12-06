
all: one two three

one:

	python /home/student/git_repo/sdn_dumps/script_fetch.py 
two:
	sh /home/student/git_repo/sdn_dumps/git_push.sh

three:
	sh /home/student/git_repo/sdn_dumps/git_push.sh
