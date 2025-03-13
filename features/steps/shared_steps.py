from behave import given, when, then

@given('I am logged in as a user')
def step_impl(context):
    print("I am logged in as a user, because i can access the context")
    print(context.__getattr__('odoo_env'))
