# Copyright (c) 2023, zhuguoqing and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class wxwork_setting(Document):
    def before_save(self):
        pass
