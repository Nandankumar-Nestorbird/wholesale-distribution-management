
import frappe
from frappe import _


def execute(filters=None):
    filters = frappe._dict(filters or {})

    validate_filters(filters)

    columns = get_columns()
    data = get_data(filters)

    return columns, data


def validate_filters(filters):

    if not filters.get("company"):
        frappe.throw(_("Please select Company"))

    if not filters.get("from_date"):
        frappe.throw(_("Please select From Date"))

    if not filters.get("to_date"):
        frappe.throw(_("Please select To Date"))

    if filters.from_date > filters.to_date:
        frappe.throw(_("From Date cannot be after To Date"))


def get_columns():

    return [
        {
            "label": _("Customer"),
            "fieldname": "customer",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 180
        },
        {
            "label": _("Total Invoices"),
            "fieldname": "total_invoices",
            "fieldtype": "Int",
            "width": 110
        },
        {
            "label": _("Total Sales"),
            "fieldname": "total_sales",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 140
        },
        {
            "label": _("Sales Returns"),
            "fieldname": "sales_returns",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 130
        },
        {
            "label": _("Net Sales"),
            "fieldname": "net_sales",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 140
        },
        {
            "label": _("Total Tax"),
            "fieldname": "total_tax",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 120
        },
        {
            "label": _("Total Paid"),
            "fieldname": "total_paid",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 130
        },
        {
            "label": _("Outstanding"),
            "fieldname": "outstanding",
            "fieldtype": "Currency",
            "options": "currency",
            "width": 130
        },
        {
            "label": _("Currency"),
            "fieldname": "currency",
            "fieldtype": "Data",
            "hidden": 1
        }
    ]


def get_data(filters):

    conditions = """
        si.company = %(company)s
        AND si.docstatus = 1
        AND si.posting_date BETWEEN %(from_date)s AND %(to_date)s
    """

    if filters.get("customer"):
        conditions += """
            AND si.customer = %(customer)s
        """

    query = """
        SELECT
            si.customer AS customer,

            COUNT(
                CASE
                    WHEN IFNULL(si.is_return, 0) = 0
                    THEN si.name
                END
            ) AS total_invoices,

            SUM(
                CASE
                    WHEN IFNULL(si.is_return, 0) = 0
                    THEN si.base_grand_total
                    ELSE 0
                END
            ) AS total_sales,

            SUM(
                CASE
                    WHEN IFNULL(si.is_return, 0) = 1
                    THEN ABS(si.base_grand_total)
                    ELSE 0
                END
            ) AS sales_returns,

            SUM(
                CASE
                    WHEN IFNULL(si.is_return, 0) = 0
                    THEN si.base_grand_total
                    ELSE -ABS(si.base_grand_total)
                END
            ) AS net_sales,

            SUM(
                CASE
                    WHEN IFNULL(si.is_return, 0) = 0
                    THEN si.base_total_taxes_and_charges
                    ELSE -ABS(si.base_total_taxes_and_charges)
                END
            ) AS total_tax,

            SUM(
                CASE
                    WHEN IFNULL(si.is_return, 0) = 0
                    THEN ABS(si.base_paid_amount)
                    ELSE -ABS(si.base_paid_amount)
                END
            ) AS total_paid,

            SUM(si.outstanding_amount * si.conversion_rate) AS outstanding,

            company.default_currency AS currency

        FROM
            `tabSales Invoice` si

        INNER JOIN
            `tabCompany` company
            ON company.name = si.company

        WHERE
            {conditions}

        GROUP BY
            si.customer,
            company.default_currency

        ORDER BY
            net_sales DESC
    """.format(conditions=conditions)

    data = frappe.db.sql(
        query,
        {
            "company": filters.company,
            "from_date": filters.from_date,
            "to_date": filters.to_date,
            "customer": filters.get("customer")
        },
        as_dict=True
    )

    return data
