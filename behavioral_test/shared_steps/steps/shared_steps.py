from behave import given, when, then
import logging

logger = logging.getLogger(__name__)

@given('I am logged in as a user')
def step_impl(context):
    logger.info("I am logged in as a user")
    logger.info(context.odoo_env)
    