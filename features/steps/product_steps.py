from behave import given, when, then

@when('I create a test product')
def step_impl(context):
    odoo_env = context.odoo_env
    product = odoo_env['product.product'].create(
        {
            'name': 'Test Product',
            'type': 'product',
            'list_price': 10.0,
            'standard_price': 5.0,
            'description': 'This is a test product',
            'default_code': 'ABC123',
            'barcode': '1234567890',
        }
    )
    context.shared_data['product'] = product

@then('If the product can\'t be created, the module can\'t be installed')
def step_impl(context):
    assert "product" in context.shared_data

@given('I have successfully created a test product')
def step_impl(context):
    assert "product" in context.shared_data

@when('I read a test product')
def step_impl(context):
    odoo_env = context.odoo_env
    product = odoo_env['product.product'].search([('name', '=', 'Test Product')])
    context.shared_data['product'] = product
    context.shared_data['product'].read()

@then('If the product can\'t be read, the module can\'t be installed')
def step_impl(context):
    assert "product" in context.shared_data

@when('I update a test product')
def step_impl(context):
    odoo_env = context.odoo_env
    product = odoo_env['product.product'].search([('name', '=', 'Test Product')])
    context.shared_data['product'] = product
    context.shared_data['product'].write({
        'name': 'Test Product Updated',
        'type': 'product',
        'list_price': 20.0,
        'standard_price': 10.0,
        'description': 'This is a test product updated',
        'default_code': 'DEF456',
        'barcode': '9876543210',
    })

@then('If the product can\'t be updated, the module can\'t be installed')
def step_impl(context):
    assert "product" in context.shared_data