import frappe
from frappe.utils import nowdate, now_datetime

@frappe.whitelist(allow_guest=True)
def change_room_status_based_on_date_range():
    # Get today's date and time
    current_date = nowdate()
    current_datetime = now_datetime()
    
    invoices_er = []
    
    # Fetch sales invoices with the required fields
    sales_invoices = frappe.db.get_all("Sales Invoice",
                                       fields=["name", "custom_selected_project", "custom_room_status", "posting_date", "custom_end_dates"],
                                       filters={
                                           "docstatus": 1  # Only consider submitted sales invoices
                                       },
                                       ignore_permissions=True)

    # Loop through the Sales Invoices
    for invoice in sales_invoices:
        posting_date = invoice.get("posting_date")
        end_date = invoice.get("custom_end_dates")
        
        if posting_date and end_date:
            # Check if the current date is within the date range
            if posting_date <= current_date <= end_date:
                # Fetch the Project DocType record
                property_name = invoice["custom_selected_project"]
                if property_name:
                    property_doc = frappe.get_doc("Project", property_name)
                    
                    # Update status to "Booked" if within the date range
                    if property_doc.custom_room_status != "Booked":
                        property_doc.custom_room_status = "Booked"
                        property_doc.flags.ignore_permissions = True
                        property_doc.save()
                        frappe.db.commit()
                        invoices_er.append(invoice)
            else:
                # Update status to "Open" if outside the date range
                property_name = invoice["custom_selected_project"]
                if property_name:
                    property_doc = frappe.get_doc("Project", property_name)
                    
                    if property_doc.custom_room_status != "Open":
                        property_doc.custom_room_status = "Open"
                        property_doc.flags.ignore_permissions = True
                        property_doc.save()
                        frappe.db.commit()
                        invoices_er.append(invoice)

    return invoices_er
