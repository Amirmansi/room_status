



import frappe
from frappe.utils import nowdate
from frappe.utils import now_datetime


@frappe.whitelist(allow_guest=True)
def change_room_status_from_booked_to_open():
    # Get today's date
    current_date = nowdate()
    current_datetime = now_datetime()

    invoices_er = []
    
    # Fetch sales invoices where custom_room_status is "Open" and check if custom_end_date has passed
    sales_invoices = frappe.db.get_all("Sales Invoice",
                                       fields=["name", "custom_selected_project", "custom_room_status", "custom_end_dates"],
                                       filters={
                                        #    "custom_room_status": "Open",
                                           "docstatus": 1  # Only consider submitted sales invoices,
                                           
                                       },ignore_permissions=True,)

    # Loop through the Sales Invoices
    for invoice in sales_invoices:
        # Check if custom_end_date has passed
        if invoice["custom_end_dates"] and invoice["custom_end_dates"] <= current_datetime:
            invoices_er.append(invoice)
            # Get the linked property from the "property" field
            property_name = invoice["custom_selected_project"]
            if property_name:
                # Fetch the Property DocType record
                property_doc = frappe.get_doc("Project", property_name)
                
                # Check if the room is currently booked
                if property_doc.custom_room_status == "Booked":
                    print("room is currently",property_doc.name)
                    # Change status to "Open"
                    property_doc.custom_room_status = "Open"
                    property_doc.flags.ignore_permissions = True
                    property_doc.save()
                frappe.db.commit()  # Commit the changes to the database

    return invoices_er
