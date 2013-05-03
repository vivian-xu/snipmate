import commands

def is_version_expt(package, version):
	version_info = "^Version: {}-[0-9]ubuntu".format(version)
	shell_cmd = 'dpkg -s {} | grep -e "{}"'.format(package, version_info)
	return commands.getoutput(shell_cmd)

def get_check_list(config_file):
	check_list = set()
	try:
		f=open(config_file)
	except Exception as e:
		print(e)
	else:
		for items in f.readlines():
			package, version = items.strip('\n ').split('=')
			check_list.add( (package.strip(' '), version.strip(' ')) )
	return check_list

if __name__=='__main__':
	config_file = 'package_required.ini'
	check_list = get_check_list(config_file)
	error_list = set()
	for package, version in check_list:
		if is_version_expt(package, version):
			print("ok | {} checked".format(package))
		else:
			print("error | {} required: {}".format(package, version))
			error_list.add(package)

	print("-"*30)  # break line

	if len(error_list) > 0:
		print("error list: {}".format(', '.join(error_list)))
	else:
		print("all checked, ok")
