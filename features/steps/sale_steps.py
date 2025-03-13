from behave import given, when, then

@given('I´ve successfully created a test partner')
def step_impl(context):
    assert "partner" in context.shared_data

@when('I create a test sale order')
def step_impl(context):
    print("When I create a test sale order")
    odoo_env = context.odoo_env

    # Create a sale order with correct order_line format
    sale_order = odoo_env['sale.order'].create({
        'name': 'Test Sale Order',
        'partner_id': context.shared_data['partner'].id,
        'order_line': [
            (0, 0, {  # ✅ Use (0, 0, {dict}) format for One2many fields
                'product_id': context.shared_data['product'].id,
                'product_uom_qty': 1,
                'product_uom': context.shared_data['product'].uom_id.id,
                'price_unit': 10.0,
            })
        ]
    })

    context.shared_data['sale_order'] = sale_order
@given('I have successfully created a test sale')
def step_impl(context):    
    assert "sale_order" in context.shared_data


@then('If the sale can\'t be read, the module can\'t be installed')
def step_impl(context):
    assert "sale_order" in context.shared_data


@then('If the sale can\'t be updated, the module can\'t be installed')
def step_impl(context):
    assert "sale_order" in context.shared_data

@when('I read a test sale')
def step_impl(context):
    odoo_env = context.odoo_env
    sale_order = odoo_env['sale.order'].search([('name', '=', 'Test Sale Order')])
    context.shared_data['sale_order'] = sale_order
    context.shared_data['sale_order'].read()


@when('I update a test sale')
def step_impl(context):
    odoo_env = context.odoo_env
    sale_order = odoo_env['sale.order'].search([('name', '=', 'Test Sale Order')], limit=1)

    if not sale_order:
        raise ValueError("Sale order not found!")

    context.shared_data['sale_order'] = sale_order

    sale_order.write({
        'name': 'Test Sale Order Updated',
        'order_line': [
            (0, 0, {  # ✅ Correct One2many format
                'product_id': context.shared_data['product'].id,
                'product_uom_qty': 20,
                'product_uom': context.shared_data['product'].uom_id.id,
                'price_unit': 10.0,
            })
        ]
    })

    print(f"✅ Sale order updated: {sale_order.name}")



@when('I confirm a test sale')
def step_impl(context):
    context.shared_data['sale_order'].action_confirm()

@then('If the sale can\'t be confirmed, the module can\'t be installed')
def step_impl(context):
    assert "sale_order" in context.shared_data


@when('I cancel a test sale')
def step_impl(context):
    context.shared_data['sale_order'].action_cancel()

@then('If the sale can\'t be cancelled, the module can\'t be installed')
def step_impl(context):
    assert "sale_order" in context.shared_data


@when('I set test sale to draft (quotation)')
def step_impl(context):
    context.shared_data['sale_order'].action_draft()

@then('If the sale can\'t be set to draft, the module can\'t be installed')
def step_impl(context):
    assert "sale_order" in context.shared_data

@then('If the sale can\'t be set to draft (quotation), the module can\'t be installed')
def step_impl(context):
    assert "sale_order" in context.shared_data