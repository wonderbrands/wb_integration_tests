from behave import given, when, then
import traceback

@when('I create a partner')
def step_impl(context):
    try:
        odoo_env = context.odoo_env
        partner = odoo_env['res.partner'].create(
            {
                'name': 'Test Partner',
                'phone': '1234567890',
                'email': 'l7MnD@example.com',
                'street': '123 Main St',
                'city': 'Anytown',
                'country_id': 1,
                'zip': '12345',
            }
        )
        context.shared_data['partner'] = partner
    except Exception as e:
        print(traceback.format_exc())
        print(f"Error creating partner: {e}")


@then('if the partner can\'t be created, the module can\'t be installed')
def step_impl(context):
    assert "partner" in context.shared_data
        
@given('I have successfully created a test partner')
def step_impl(context):
    assert "partner" in context.shared_data

@when('I read a test partner')
def step_impl(context):
    odoo_env = context.odoo_env
    partner = odoo_env['res.partner'].search([('name', '=', 'Test Partner')])[0]
    context.shared_data['partner'] = partner
    context.shared_data['partner'].read()

@when('If the partner can\'t be read, the module can\'t be installed')
def step_impl(context):
    assert "partner" in context.shared_data

@when('I update a test partner')
def step_impl(context):
    odoo_env = context.odoo_env
    context.shared_data['partner'].write(
        {
            'name': 'Updated Test Partner',
            'email': 'l7MnD@example.com',
            'phone': '1234567890',
            'street': '321 Main St',
            'city': 'Anytown_1',
            'country_id': 2,
            'zip': '54321',
        }
    )

@then('If the partner can\'t be updated, the module can\'t be installed')
def step_impl(context):
    assert "partner" in context.shared_data

@then('If the partner can\'t be read, the module can\'t be installed')
def step_impl(context):
    assert "partner" in context.shared_data