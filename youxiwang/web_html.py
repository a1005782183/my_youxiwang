from flask_wtf import csrf
from flask import Blueprint, current_app, make_response

# 提供静态文件的蓝图
html = Blueprint("web_html", __name__)

@html.route("/<re(r'.*'):html_file_name>")
def get_html(html_file_name):
	"""提供html静态文件"""

	if not html_file_name:
		html_file_name = "login.html"

	html_file_name = "html/" + html_file_name

	# 创建一个csrf_token值
	csrf_token = csrf.generate_csrf()

	resp = make_response(current_app.send_static_file(html_file_name))

	resp.set_cookie("csrf_token", csrf_token)

	return resp