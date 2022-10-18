import glob
import re
github_organization = "CMPS-6100"
github_repo = "notebooks"
def get_header(fname):
	try:
		return re.sub('#', '', open(fname).readlines()[0]).strip()
	except Exception as e:
		return 'name'

for module in sorted(glob.glob("[0-9][0-9]-*")):
	module_title = '**{}**'.format(get_header('{}/README.md'.format(module)))
	print('|[{}](https://github.com/{}/{}/tree/main/{})|'.format(module_title, github_organization, github_repo, module))
	for lecture in sorted(glob.glob('{}/0*'.format(module))):
		lecture_title = lecture.split('/')[1][3:-6] # 01-selection_sort.ipynb -> selection_sort
		lecture_title = " ".join(lecture_title.split("_")).title() # selection_sort -> Selection Sort
		static_link = "https://nbviewer.jupyter.org/github/{}/{}/blob/main/{}?flush_cache=True".format(github_organization, github_repo, lecture)
		live_link = "https://mybinder.org/v2/gh/{}/{}/main?filepath={}".format(github_organization, github_repo, lecture)
		ipynb = '&nbsp;&nbsp;*{}* &nbsp;&nbsp; [live]({}) / [static]({})'.format(lecture_title, live_link, static_link)

		print('|{}|'.format(ipynb))
