
import frappe
from frappe import _
from frappe.utils import flt


@frappe.whitelist()
def get_item_stock_by_warehouse(item_code=None):
    """
    Return warehouse-wise stock availability for an Item.

    API:
    /api/method/wholesale_distribution.api.get_item_stock_by_warehouse

    Input:
    item_code = ELE-001
    """

    # 1. Validate input
    if not item_code or not isinstance(item_code, str):
        frappe.throw(_("Please provide a valid Item Code."))

    item_code = item_code.strip()

    if not item_code:
        frappe.throw(_("Item Code cannot be empty."))

    # 2. Check Item read permission
    if not frappe.has_permission("Item", "read", doc=item_code):
        frappe.throw(
            _("You are not permitted to access this Item."),
            frappe.PermissionError
        )

    # 3. Check whether Item exists
    if not frappe.db.exists("Item", item_code):
        frappe.throw(
            _("Item {0} does not exist.").format(item_code),
            frappe.DoesNotExistError
        )

    # 4. Check Bin read permission
    if not frappe.has_permission("Bin", "read"):
        frappe.throw(
            _("You are not permitted to access stock information."),
            frappe.PermissionError
        )

    # 5. Fetch warehouse-wise stock
    # get_list respects user permissions and permission query conditions.
    bins = frappe.get_list(
        "Bin",
        filters={
            "item_code": item_code
        },
        fields=[
            "warehouse",
            "actual_qty",
            "reserved_qty",
            "projected_qty"
        ],
        order_by="warehouse asc",
        limit_page_length=1000
    )

    # 6. Prepare response
    warehouses = []

    for row in bins:
        warehouses.append({
            "warehouse": row.warehouse,
            "actual_qty": flt(row.actual_qty),
            "reserved_qty": flt(row.reserved_qty),
            "projected_qty": flt(row.projected_qty)
        })

    # 7. Return JSON response
    return {
        "item_code": item_code,
        "warehouses": warehouses
    }
