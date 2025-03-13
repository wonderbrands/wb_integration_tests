from behave import given, when, then

@when('I create a test stock location')
def step_impl(context):
    odoo_env = context.odoo_env
    stock_location = odoo_env['stock.location'].create(
        {
            'name': 'Test Stock Location',
            'usage': 'internal',
        }
    )
    context.shared_data['stock_location'] = stock_location

@then('if the stock location can\'t be created, the module can\'t be installed')
def step_impl(context):
    assert "stock_location" in context.shared_data


@given('I have successfully created a test stock location')
def step_impl(context):    
    assert "stock_location" in context.shared_data

@when('I add product qty to test stock location')
def step_impl(context):
    odoo_env = context.odoo_env
    stock_location = context.shared_data['stock_location']
    product = context.shared_data['product']
    qty = odoo_env['stock.quant'].create(
        {
            'product_id': product.id,
            'location_id': stock_location.id,
            'quantity': 10,
        }
    )
    context.shared_data['qty'] = qty

@then('if the product qty can\'t be added to the stock location, the module can\'t be installed')
def step_impl(context):
    assert "qty" in context.shared_data

@when('I create a test stock transfer')
def step_impl(context):
    odoo_env = context.odoo_env
    stock_location = context.shared_data['stock_location']
    product = context.shared_data['product']
    qty = context.shared_data['qty']

    # Get the destination location (Customer)
    location_dest = odoo_env['stock.location'].search([('usage', '=', 'customer')], limit=1)
    if not location_dest:
        raise ValueError("Customer location not found!")

    # Create the stock picking (transfer)
    stock_transfer = odoo_env['stock.picking'].create({
        'location_id': stock_location.id,
        'location_dest_id': location_dest.id,
        'partner_id': context.shared_data['partner'].id,
        'sale_id': context.shared_data['sale_order'].id,
        'picking_type_id': odoo_env.ref('stock.picking_type_in').id,
        'move_ids_without_package': [
            (0, 0, {  # ✅ Correct One2many format
                'name': f'Move for {product.display_name}',
                'product_id': product.id,
                'product_uom': product.uom_id.id,
                'product_uom_qty': qty.quantity,
                'location_id': stock_location.id,
                'location_dest_id': location_dest.id,
            })
        ]
    })

    context.shared_data['stock_transfer'] = stock_transfer
    print(f"✅ Stock Transfer Created: {stock_transfer.name}")


@then('if the stock transfer can\'t be created, the module can\'t be installed')
def step_impl(context):
    assert "stock_transfer" in context.shared_data

@when('I read a test stock location')
def step_impl(context):
    odoo_env = context.odoo_env
    stock_location = odoo_env['stock.location'].search([('name', '=', 'Test Stock Location')])
    context.shared_data['stock_location'] = stock_location
    context.shared_data['stock_location'].read()

@then('If the stock location can\'t be read, the module can\'t be installed')
def step_impl(context):
    assert "stock_location" in context.shared_data

@when('I update a test stock location')
def step_impl(context):
    context.shared_data['stock_location'].write(
        {
            'name': 'Test Stock Location Updated',
        }
    )

@then('If the stock location can\'t be updated, the module can\'t be installed')
def step_impl(context):
    assert "stock_location" in context.shared_data

@when('I read the quantity of a product in a test stock location')
def step_impl(context):
    odoo_env = context.odoo_env
    stock_location = context.shared_data['stock_location']
    product = context.shared_data['product']
    qty = odoo_env['stock.quant'].search([('product_id', '=', product.id), ('location_id', '=', stock_location.id)])
    context.shared_data['qty'] = qty
    context.shared_data['qty'].read()

@then('If the qty can\'t be read, the module can\'t be installed')
def step_impl(context):
    assert "qty" in context.shared_data

@when('I update the quantity of a product in a test stock location')
def step_impl(context):
    context.shared_data['qty'].write(
        {
            'quantity': 20,
        }
    )

@then('If the qty can\'t be updated, the module can\'t be installed')
def step_impl(context):    
    assert "qty" in context.shared_data
    assert context.shared_data['qty'].quantity == 20

@when('I read a test stock transfer')
def step_impl(context):
    odoo_env = context.odoo_env
    stock_transfer = odoo_env['stock.picking'].search([('name', '=', 'Test Stock Transfer')])
    context.shared_data['stock_transfer'] = stock_transfer
    context.shared_data['stock_transfer'].read()

@then('If the stock transfer can\'t be read, the module can\'t be installed')
def step_impl(context):
    assert "stock_transfer" in context.shared_data

@when('I update a test stock transfer')
def step_impl(context):
    qty = context.shared_data['qty']
    product = context.shared_data['product']
    stock_location = context.shared_data['stock_location']
    odoo_env = context.odoo_env

    stock_transfer = context.shared_data['stock_transfer']

    # Get the new destination location (Customer)
    location_dest = odoo_env['stock.location'].search([('usage', '=', 'customer')], limit=1)
    if not location_dest:
        raise ValueError("Customer location not found!")

    # Correct format for One2many update
    stock_transfer.write({
        'name': 'Test Stock Transfer Updated',
        'location_dest_id': location_dest.id,
        'partner_id': context.shared_data['partner'].id,
        'sale_id': context.shared_data['sale_order'].id,
        'picking_type_id': odoo_env.ref('stock.picking_type_in').id,
        'move_ids_without_package': [
            (0, 0, {  # ✅ Correct format for One2many
                'name': f'Move for {product.display_name}',
                'product_id': product.id,
                'product_uom': product.uom_id.id,
                'product_uom_qty': qty.quantity,
                'location_id': stock_location.id,
                'location_dest_id': location_dest.id,
            })
        ],
    })

    print(f"✅ Stock Transfer Updated: {stock_transfer.name}")


@then('If the stock transfer can\'t be updated, the module can\'t be installed')
def step_impl(context):
    assert "stock_transfer" in context.shared_data

@given('I have successfully added product qty to test stock location')
def step_impl(context):
    odoo_env = context.odoo_env
    stock_location = context.shared_data['stock_location']
    product = context.shared_data['product']
    qty = odoo_env['stock.quant'].search([('product_id', '=', product.id), ('location_id', '=', stock_location.id)])
    context.shared_data['qty'] = qty

@given('I have successfully created a test sale order')
def step_impl(context):
    assert "sale_order" in context.shared_data



@given('I have successfully created a test stock transfer')
def step_impl(context):
    assert "stock_transfer" in context.shared_data

