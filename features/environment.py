def before_all(context):
    context.shared_data = {}

def after_all(context):
    deletion_order = [
        'stock_picking',
        'qty',
        'stock_location',
        'sale_order',
        'product',
        'partner',
    ]
    for record in deletion_order:
        try:
            if record in context.shared_data.keys():
                if record == 'sale_order':
                    context.shared_data[record].action_cancel()
                context.shared_data[record].unlink()
        except Exception as e:
            _logger.error(f"❌ Error deleting {record}: {e}")
    context.odoo_env = None
    context.shared_data.clear()