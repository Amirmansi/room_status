app_name = "room_status"
app_title = "Room Status"
app_publisher = "Mohamed Sabour"
app_description = "Change room Status"
app_email = "eng.mohammed.sabour@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/room_status/css/room_status.css"
# app_include_js = "/assets/room_status/js/room_status.js"

# include js, css files in header of web template
# web_include_css = "/assets/room_status/css/room_status.css"
# web_include_js = "/assets/room_status/js/room_status.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "room_status/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "room_status.utils.jinja_methods",
# 	"filters": "room_status.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "room_status.install.before_install"
# after_install = "room_status.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "room_status.uninstall.before_uninstall"
# after_uninstall = "room_status.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "room_status.utils.before_app_install"
# after_app_install = "room_status.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "room_status.utils.before_app_uninstall"
# after_app_uninstall = "room_status.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "room_status.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"room_status.tasks.all"
# 	],
# 	"daily": [
# 		"room_status.tasks.daily"
# 	],
# 	"hourly": [
# 		"room_status.tasks.hourly"
# 	],
# 	"weekly": [
# 		"room_status.tasks.weekly"
# 	],
# 	"monthly": [
# 		"room_status.tasks.monthly"
# 	],
# }


# hooks.py

scheduler_events = {
    "cron": {
        "*/2 * * * *": [  # Runs the job every 3 minutes
            "room_status.change_room_status.change_room_status_from_booked_to_open"
        ]
    },
}


# Testing
# -------

# before_tests = "room_status.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "room_status.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "room_status.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["room_status.utils.before_request"]
# after_request = ["room_status.utils.after_request"]

# Job Events
# ----------
# before_job = ["room_status.utils.before_job"]
# after_job = ["room_status.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"room_status.auth.validate"
# ]
