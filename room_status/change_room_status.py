import frappe
from frappe.utils import nowdate

@frappe.whitelist(allow_guest=True)
def change_room_status_based_on_date_range():
    # Get today's date
    current_date = nowdate()
    
    updated_invoices = []
    
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
        
        # Ensure both posting date and end date are present
        if posting_date and end_date:
            project_name = invoice["custom_selected_project"]
            if project_name:
                project_doc = frappe.get_doc("Project", project_name)
                
                # Check if the current date is within the date range
                if posting_date <= current_date <= end_date:
                    # Update status to "Booked" if within the date range
                    if project_doc.custom_room_status != "Booked":
                        project_doc.custom_room_status = "Booked"
                        project_doc.flags.ignore_permissions = True
                        project_doc.save()
                        updated_invoices.append(invoice)
                else:
                    # Update status to "Open" if outside the date range
                    if project_doc.custom_room_status != "Open":
                        project_doc.custom_room_status = "Open"
                        project_doc.flags.ignore_permissions = True
                        project_doc.save()
                        updated_invoices.append(invoice)
    
    # Return the list of updated invoices
    return updated_invoices
